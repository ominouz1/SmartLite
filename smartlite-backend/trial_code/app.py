# app.py

from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from sensor_control import control_light, manual_control, get_light_status, cleanup_gpio
import threading
import atexit

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")  # Allow WebSocket connections from this origin

# Start the sensor monitoring in a separate thread
def start_sensor_monitoring():
    thread = threading.Thread(target=control_light, args=(socketio,))
    thread.daemon = True
    thread.start()

@app.route('/status', methods=['GET'])
def status():
    """API to get the current light status."""
    status = get_light_status()
    return jsonify({'light_status': status})

@app.route('/manual-toggle', methods=['POST'])
def manual_toggle():
    """API to manually control the light."""
    data = request.json
    status = data.get('light_status')
    if status is not None:
        updated_status = manual_control(status)
        # Notify connected clients via WebSocket
        socketio.emit('status_update', {'light_status': updated_status})
        return jsonify({'status': 'success', 'light_status': updated_status})
    return jsonify({'status': 'error', 'message': 'Invalid input'}), 400

@socketio.on('connect')
def handle_connect():
    """Notify the new client of the current light status when they connect."""
    current_status = get_light_status()
    emit('status_update', {'light_status': current_status})

if __name__ == '__main__':
    # Start the sensor monitoring in a separate thread
    start_sensor_monitoring()

    # Ensure GPIO cleanup on exit
    atexit.register(cleanup_gpio)

    # Run the Flask app with WebSocket support
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
