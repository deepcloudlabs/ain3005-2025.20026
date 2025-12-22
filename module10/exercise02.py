import asyncio
import websockets
import json
import pika
from rx import operators as ops
from rx.subject import Subject
from rx.scheduler.eventloop import AsyncIOScheduler

BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"
RABBITMQ_QUEUE = "filtered_trades"

# RabbitMQ Connection Setup
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue=RABBITMQ_QUEUE)

# Reactive Stream Setup
subject = Subject()


async def binance_websocket():
    """Connect to Binance WebSocket and emit data to the subject."""
    async with websockets.connect(BINANCE_WS_URL) as websocket:
        async for message in websocket:
            trade = json.loads(message)
            subject.on_next(trade)


def process_trades():
    """Filter, map, reduce and send results to RabbitMQ."""
    scheduler = AsyncIOScheduler(asyncio.get_event_loop())  # Attach scheduler to event loop

    subject.pipe(
        ops.filter(lambda trade: (float(trade['p'])*float(trade['q'])) > 10_000),  # Example filter: price > 30,000
        ops.map(lambda trade: {
            "symbol": trade["s"],
            "price": float(trade["p"]),
            "quantity": float(trade["q"]),
            "timestamp": trade["T"]
        }),
        ops.buffer_with_time(30.0, scheduler=scheduler),  # 30-second time window
        ops.map(lambda trades: {
            "average_price": sum(t["price"] * t["quantity"] for t in trades) / sum(
                t["quantity"] for t in trades) if trades else None,
            "total_quantity": sum(t["quantity"] for t in trades),
            "window_start": trades[0]["timestamp"] if trades else None,
            "window_end": trades[-1]["timestamp"] if trades else None,
        }),
    ).subscribe(
        on_next=lambda result: send_to_rabbitmq(result),
        on_error=lambda e: print(f"Error: {e}"),
        on_completed=lambda: print("Processing completed."),
    )


def send_to_rabbitmq(result):
    """Send processed trade data to RabbitMQ."""
    if result["average_price"] is not None:
        channel.basic_publish(
            exchange="",
            routing_key=RABBITMQ_QUEUE,
            body=json.dumps(result)
        )
        print(f"Sent to RabbitMQ: {result}")


async def main():
    """Main event loop."""
    # Start WebSocket connection
    websocket_task = asyncio.create_task(binance_websocket())

    # Start processing trades
    process_trades()

    # Run WebSocket task indefinitely
    await websocket_task


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down...")
        connection.close()