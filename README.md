# Mouse-Capture

Mouse-Capture is a simple project that captures and displays real-time mouse coordinates and captures images upon mouse clicks using a WebSocket server.

## Table of Contents

-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [Usage](#usage)
    -   [Starting the Server](#starting-the-server)
    -   [Connecting to WebSocket](#connecting-to-websocket)
-   [Project Structure](#project-structure)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

-   [Python](https://www.python.org/) (3.9 or higher)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Antonio0512/Mouse-Capturer.git
    cd Mouse-Capture
    ```

2. Create a virtual environment (venv). For Windows:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

    For Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Starting the HTTP Server

1. Open a terminal and navigate to the server folder.

2. Run the HTTP Server

    ```bash
    python server.py
    ```

3. The HTTP server will start, and you should see a message indicating the server has started.

4. Keep the terminal open to ensure the WebSocket server remains active.

### Starting the Web Socket Server

1. Open a terminal and navigate to the project root directory.

2. Run the WebSocket server:

    ```bash
    python main.py
    ```

3. The WebSocket server will start, and you should see a message indicating the server has started.

4. Keep the terminal open to ensure the WebSocket server remains active.

## Project Structure

```
├── client
│ └── index.html
├── database
│ └── coords_images.db
│ └── database.py
├── server
│ └── server.py
├── websocket
│ └── websocket.py
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```
