import socketio

SERVER_URL = "ws://localhost:7001/socket.io"  # change to your server

sio = socketio.Client(
    reconnection=True,
    reconnection_attempts=0,   # 0 = infinite
    reconnection_delay=1,
    reconnection_delay_max=5,
)

@sio.event
def connect():
    print("connected:", sio.sid)

@sio.event
def connect_error(data):
    print("connect_error:", data)

@sio.event
def disconnect():
    print("disconnected")

@sio.on("fire")
def on_fire(payload):
    print("fire event received:", payload)

@sio.on("hire")
def on_hire(payload):
    print("hire event received:", payload)

@sio.on("update")
def on_update(payload):
    print("update event received:", payload)

if __name__ == "__main__":
    # If your server is Socket.IO, it’s typically on /socket.io (default)
    sio.connect(
        SERVER_URL,
        transports=["websocket", "polling"],  # try websocket first; polling fallback
        wait=True,
        wait_timeout=10,
    )
    sio.wait()  # keep process alive to receive events
