import asyncio
import websockets
import json
from rx import operators as ops
from rx.scheduler.eventloop import AsyncIOScheduler
from rx.subject import Subject

def process_message(msg):
    """Process the received message from Binance."""
    try:
        data = json.loads(msg)
        if "data" in data and "p" in data["data"]:
            return float(data["data"]["p"])
    except Exception as e:
        print(f"Error processing message: {e}")
    return None

async def binance_ws_stream(trade_pairs):
    """Connect to Binance WebSocket and stream data."""
    url = f"wss://stream.binance.com:9443/stream?streams={'/'.join(trade_pairs)}"
    async with websockets.connect(url) as websocket:
        async for message in websocket:
            yield message

async def main():
    #trade_pairs = ["btcusdt@trade", "ethusdt@trade"]  # Add pairs as needed
    trade_pairs = ["btcusdt@trade"]  # Add pairs as needed

    subject = Subject()

    async def websocket_task():
        async for message in binance_ws_stream(trade_pairs):
            subject.on_next(message)

    scheduler = AsyncIOScheduler(asyncio.get_event_loop())

    subject.pipe(
        ops.map(process_message),
        ops.filter(lambda x: x is not None),
        ops.buffer_with_time(30, scheduler=scheduler),
        ops.map(lambda prices: {
            "count": len(prices),
            "average": sum(prices) / len(prices) if prices else None,
            "min": min(prices) if prices else None,
            "max": max(prices) if prices else None,
        })                                            # Map: Aggregate results
    ).subscribe(
        lambda stats: print(f"Stats in 30s window: {stats}"),
        lambda e: print(f"Error: {e}"),
        lambda: print("Stream completed.")
    )

    await websocket_task()

if __name__ == "__main__":
    asyncio.run(main())