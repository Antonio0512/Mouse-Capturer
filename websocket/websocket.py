import os
from dotenv import load_dotenv
from datetime import datetime
import cv2
import asyncio
import pyautogui
import websockets
from database.database import DatabaseManager

load_dotenv()

database = DatabaseManager()

HOST = os.environ.get("HOST_WS", "localhost")
PORT = int(os.environ.get("PORT_WS", "8000"))

async def setup_websocket(websocket):

    # Gets the current event loop 
    loop = asyncio.get_event_loop()

    # Creates two tasks 
    tasks1 = loop.create_task(feed_coords(websocket))
    tasks2 = loop.create_task(read_clicks(websocket))

    # Waits until both tasks are completed
    await asyncio.wait([tasks1, tasks2])


def get_mouse_position():
    coords = pyautogui.position()
    return coords[0], coords[1]


def capture_image(path: str, camera_port: int = 0):

    # Creates a VideoCapture object to connect to the camera
    camera = cv2.VideoCapture(camera_port)

    # Captures a single frame from the camera
    _, camera_capture = camera.read()

    # Saves the captured frame as an image file at a path
    cv2.imwrite(path, camera_capture)

    # Turns the captured frame in a PNG image and returns the binary representation of the image
    _, buffer = cv2.imencode(".png", camera_capture)

    return buffer


async def feed_coords(websocket):

    # Infinitely sending mouse coordinates
    while True:
        coords = get_mouse_position()

        # Sending the coordinates as a string to the websocket
        await websocket.send(str(coords))


def on_click(incoming_coords: str):

    # Path to where the image would be saved
    media_path = os.path.join(os.path.dirname(__file__), '../media')
    os.makedirs(media_path, exist_ok=True)

    # Capture an image
    image = capture_image(os.path.join(media_path, f'{datetime.now()}.png'))

    # Inserts the coordinates and captured image into the database
    database.insert_data(incoming_coords, image)


async def read_clicks(websocket):
    
    # Infinitely receiving data from the websocket
    while True:
        data = await websocket.recv()

        on_click(data)

        await asyncio.sleep(0.1)


def start_websocket_server():
    database.setup()
    start_server = websockets.serve(
        setup_websocket, HOST, PORT,
)
    print(f"Web socket started - http://{HOST}:{PORT}")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
