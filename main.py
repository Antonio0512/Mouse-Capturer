import asyncio
import threading
from websocket.websocket import start_websocket_server
from server.server import start_http_server

async def run_servers():
    # Run the WebSocket server in a separate thread
    websocket_thread = threading.Thread(target=lambda: asyncio.run(start_websocket_server()))
    websocket_thread.start()

    # Run the HTTP server in the main thread
    start_http_server()

    # Wait for the WebSocket thread to finish
    # websocket_thread.join()

if __name__ == '__main__':
    asyncio.run(run_servers())
