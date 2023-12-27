# Mouse-Capture

Mouse-Capture is a simple project that captures and displays real-time mouse coordinates and captures images upon mouse clicks using a WebSocket server.

## Table of Contents

-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [Usage](#usage)
    -   [Starting the Program](#starting-the-program)
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

### Starting the program

1. Open a terminal and navigate to the root directory (where the main.py is located).
   
2. Run both servers 
    ```bash
    python main.py
    ```
    You can use your IDE, too.
    
3. The HTTP and Websocket servers will start simultaneously, and you should see messages indicating both servers have started.

4. Open your browser and type the host and port you have written in your .env file or http://localhost:8080 by default.
   
5. Keep the terminal open to ensure the WebSocket server remains active.

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
