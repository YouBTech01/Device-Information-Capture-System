# Device Information Capture System

This project is a Flask-based web application designed to capture device details in real time when a user accesses a specific URL. It collects information such as the browser name, device platform, screen resolution, battery level, IP address, and location (if enabled). The application features a hacking theme with a green-on-black style to create a visually engaging experience. 

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Code Structure](#code-structure)
- [License](#license)

## Project Overview
This device information capture system is built using Python and Flask. It is designed for educational purposes, providing insights into how various device details can be accessed and displayed in real time. When users access the site, they see a styled page with a button to send their device information to the server, which is logged in real time.

## Features
- **Real-time Device Data Collection**: Collects data including browser, platform, screen size, battery level, IP address, and location.
- **Hacking Theme**: Custom UI with green-on-black styling for a "hacking" effect.
- **Server-Side Logging**: Displays detailed information in the server logs for testing and debugging purposes.
- **JavaScript-Based Data Collection**: Utilizes JavaScript to access client-side details.

## Technology Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: None (logs information to the console)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/device-information-capture.git
    cd device-information-capture
    ```

2. **Install Dependencies**:
    ```bash
    pip install flask
    ```

3. **Run the Application**:
    ```bash
    python app.py
    ```

4. **Access the Application**:
    - Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Start the Flask server.
2. Open the provided URL in a browser.
3. Click the "Send Device Details" button to send your device information to the server.
4. The server logs will display the collected information.

## API Endpoints

### `/`
- **Method**: GET
- **Description**: Serves the main page with the "Send Device Details" button.

### `/device-info`
- **Method**: POST
- **Description**: Receives device information from the frontend and logs it to the server.

## Code Structure

- **app.py**: Main application file that sets up the Flask server, HTML template, and JavaScript functions for data collection.
- **HTML Template**: 
    - The HTML template is embedded within the Flask app and styled with inline CSS for the green-on-black hacking theme.
    - JavaScript functions collect device details using the `navigator` and `window` objects and send them to the server.

### Key Sections in `app.py`

- **HTML Template**: Defines the green-on-black hacking-themed UI with a button to trigger data capture.
- **JavaScript Functions**:
    - `sendDeviceInfo()`: Collects device information including browser details, screen size, battery level, and location.
    - `sendToServer()`: Sends the collected data to the server via a POST request to `/device-info`.
- **Server-Side Logging**: Logs data received from the client, including IP address, browser, platform, screen dimensions, battery level, and location.

## Example Output in Server Log
```plaintext
--- Device Information Received ---
IP Address      : 127.0.0.1
Browser         : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Platform        : Win32
Screen Width    : 1920
Screen Height   : 1080
Battery Level   : 80%
Is Charging     : No
Location        : { "latitude": 37.7749, "longitude": -122.4194 }
Server Time     : 2024-11-12 13:45:27
-----------------------------------
