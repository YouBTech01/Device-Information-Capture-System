from flask import Flask, request, render_template_string, jsonify
import datetime

app = Flask(__name__)

# Updated HTML template with Hacking theme (dark and green-on-black style)
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Device Information</title>
    <style>
        /* Hacking theme style */
        body, html {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Courier New', Courier, monospace;
            background-color: #0d0d0d;
            color: #00ff00;
            overflow: hidden;
        }
        #container {
            background-color: #1e1e1e;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.8);
            text-align: center;
            width: 100%;
            max-width: 600px;
        }
        h2 {
            font-size: 2rem;
            margin-bottom: 20px;
            color: #00ff00;
        }
        p {
            font-size: 1.2rem;
            color: #66ff66;
        }
        #send-info {
            padding: 12px 24px;
            font-size: 18px;
            font-weight: bold;
            color: #0d0d0d;
            background-color: #00ff00;
            border: 2px solid #00cc00;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }
        #send-info:hover {
            background-color: #00cc00;
            transform: scale(1.1);
        }
        #send-info:active {
            transform: scale(1.05);
        }
        code {
            font-size: 1rem;
            color: #ffcc00;
        }
    </style>
    <script>
        async function sendDeviceInfo() {
            const deviceDetails = {};

            // 1. Get browser and platform details
            deviceDetails.browser = navigator.userAgent;
            deviceDetails.platform = navigator.platform;

            // 2. Get screen details
            deviceDetails.screenWidth = window.screen.width;
            deviceDetails.screenHeight = window.screen.height;

            // 3. Get battery details if available
            if (navigator.getBattery) {
                const battery = await navigator.getBattery();
                deviceDetails.battery = battery.level * 100 + "%";
                deviceDetails.isCharging = battery.charging ? "Yes" : "No";
            }

            // 4. Get location details
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition((position) => {
                    deviceDetails.location = {
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude
                    };
                    console.log("Sending device details to server:", deviceDetails); // Debug log
                    sendToServer(deviceDetails);
                }, (error) => {
                    console.error("Geolocation error:", error); // Debug log for geolocation errors
                    deviceDetails.location = "Geolocation not supported or denied.";
                    sendToServer(deviceDetails);
                });
            } else {
                deviceDetails.location = "Geolocation not supported";
                sendToServer(deviceDetails);
            }
        }

        function sendToServer(deviceDetails) {
            // Send the collected data to the server
            fetch('/device-info', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(deviceDetails)
            })
            .then(response => response.json())
            .then(data => {
                alert("Device details sent successfully!");
            })
            .catch(error => {
                console.error("Error sending data to server:", error); // Debug log for sending errors
            });
        }
    </script>
</head>
<body>
    <div id="container">
        <h2>Device Information Collection</h2>
        <p>Click the button below to send your device details.</p>
        <button id="send-info" onclick="sendDeviceInfo()">Send Device Details</button>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Render the HTML with the button
    return render_template_string(html_template)

@app.route('/device-info', methods=['POST'])
def device_info():
    # Get data sent from JavaScript
    data = request.get_json()

    # Log data for debugging in Python terminal
    print("\n--- Device Information Received ---")
    print(f"IP Address      : {request.remote_addr}")
    print(f"Browser         : {data.get('browser')}")
    print(f"Platform        : {data.get('platform')}")
    print(f"Screen Width    : {data.get('screenWidth')}")
    print(f"Screen Height   : {data.get('screenHeight')}")
    print(f"Battery Level   : {data.get('battery', 'N/A')}")
    print(f"Is Charging     : {data.get('isCharging', 'N/A')}")
    print(f"Location        : {data.get('location', 'N/A')}")
    print(f"Server Time     : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------------\n")

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)