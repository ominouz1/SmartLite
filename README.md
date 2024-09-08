# SmartLite

### Team Members
- **Joshua Norvor**
- **Benjamin Wilberforce**
- **Andrew Appah**
- **Kwabena Appiagyei**

SmartLite is an intelligent lighting system designed to automate room lighting based on people entering or exiting the room. It uses ultrasonic sensors and a Raspberry Pi to detect movement and adjust the lights accordingly. The system also supports manual control via a web interface, allowing users to override the automation from anywhere.

## Features

- Automatic lighting based on room occupancy
- Real-time people counting
- Manual control via a web interface
- Remote control from anywhere with internet access

## Table of Contents

- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Wiring and Setup](#wiring-and-setup)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [License](#license)
- [Contribution](#contribution)

---

## Hardware Requirements

- Raspberry Pi (with Raspbian installed)
- 2x Ultrasonic Sensors (HC-SR04)
- LED light or a bulb (connected to GPIO pin)
- Jumper wires
- Breadboard
- Resistors (if needed for the circuit)

## Software Requirements

- Python 3.x
- Flask and Flask-SocketIO
- React (for the frontend)
- Node.js and npm (for managing frontend dependencies)
- RPi.GPIO Python library

## Wiring and Setup

### Ultrasonic Sensor (HC-SR04)

- **Sensor 1 (Placed Outside):**
  - VCC to Raspberry Pi 5V
  - GND to Raspberry Pi GND
  - TRIG to Raspberry Pi GPIO Pin 23
  - ECHO to Raspberry Pi GPIO Pin 24

- **Sensor 2 (Placed Inside):**
  - VCC to Raspberry Pi 5V
  - GND to Raspberry Pi GND
  - TRIG to Raspberry Pi GPIO Pin 27
  - ECHO to Raspberry Pi GPIO Pin 22

### Light Connection

- **Light Pin:** Connect your LED or bulb relay to GPIO Pin 18 on the Raspberry Pi.
- **Ground:** Connect the light circuit to a ground pin.

## Backend Setup

1. **Install Python dependencies:**

   ```bash
   pip install Flask Flask-SocketIO Flask-CORS RPi.GPIO
   ```

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/smartlite.git
   cd smartlite/backend
   ```

3. **Run the Flask Backend:**

   ```bash
   python app.py
   ```

   This will start the backend server, which will handle sensor input and communicate with the frontend.

### Key Backend Files

- `app.py`: Main Flask application handling API routes and WebSocket communication.
- `lighting.py`: Controls the light and keeps track of the people count.
- `sensors.py`: Manages sensor inputs and detects entry/exit events.

## Frontend Setup

1. **Install Node.js dependencies:**

   ```bash
   cd smartlite/frontend
   npm install
   ```

2. **Configure the Backend URL:**

   Ensure that `axiosConfig.js` is pointing to your Raspberry Pi’s IP address or `localhost` for development.

   Example:

   ```javascript
   const axiosInstance = axios.create({
     baseURL: 'http://127.0.0.1:5000/', // backend URL
     headers: {
       'Content-Type': 'application/json',
     },
   });
   ```

3. **Run the Frontend:**

   ```bash
   npm start
   ```

   This will launch the web interface on `http://localhost:3000`.

### Key Frontend Files

- `Home.js`: Main UI component that displays the light status, people count, and allows manual control.
- `api.js`: Contains the API calls to communicate with the backend.
- `ToggleSwitch.js`, `LightsStatus.js`, `PeopleCount.js`: Individual components for different parts of the UI.

## Running the Project

1. **Ensure the Raspberry Pi is properly wired** with the sensors and light as described above.
2. **Start the backend server** on the Raspberry Pi by running:

   ```bash
   python app.py
   ```

3. **Start the frontend** on your local machine or Raspberry Pi by running:

   ```bash
   npm start
   ```

Once both the backend and frontend are running, you can access the web interface to view the real-time status of the lights, manually control them, and track the number of people in the room.

## Usage

- **Automatic Mode:** When someone enters the room, the lights turn on automatically. If the last person exits the room, the lights will turn off.

- **Manual Mode:** You can use the web interface to manually override the lights, turning them on or off from anywhere with internet access.

  The method of light control (manual or automatic) will be displayed on the interface.

Feel free to explore and modify the code to fit your needs. If you encounter any issues or need further assistance, please refer to the issues section of the repository.

## License

This project is open-source and available under the MIT License.

## Contribution

Contributions are welcome! Please submit a pull request if you would like to contribute to this project.