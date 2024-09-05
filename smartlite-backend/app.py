from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from lighting import update_stack, set_light_manually, get_light_status
from flask_cors import CORS
import threading
import logging
from sensors import monitor_sensors

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")  # Allow WebSocket connections from this origin

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize thread-safe variables
lock = threading.Lock()
light_status = False
people_count = 0

def sensor_monitoring_wrapper():
    """Wrapper for sensor monitoring that includes WebSocket updates."""
    global light_status, people_count
    logging.info("Starting sensor monitoring thread")
    for event in monitor_sensors():
        is_entry = event.get('is_entry')
        with lock:
            people_count = update_stack(is_entry)
            light_status = get_light_status()
        notify_clients()

def notify_clients():
    """Send real-time updates to connected WebSocket clients."""
    with lock:
        socketio.emit('status_update', {
            'light_status': light_status,
            'people_count': people_count
        })

@app.route('/update', methods=['POST'])
def update():
    global light_status, people_count
    try:
        data = request.json
        is_entry = data.get('is_entry')
        with lock:
            people_count = update_stack(is_entry)
            light_status = get_light_status()
        notify_clients()
        return jsonify({'status': 'success', 'people_count': people_count, 'light_status': light_status})
    except Exception as e:
        logging.error(f"Error updating light status: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
    global light_status, people_count
    with lock:
        return jsonify({'light_status': light_status, 'people_count': people_count})

@app.route('/manual-toggle', methods=['POST'])
def manual():
    global light_status
    try:
        data = request.json
        light_status = set_light_manually(data.get('light_status'))
        notify_clients()
        return jsonify({'status': 'success', 'light_status': light_status})
    except Exception as e:
        logging.error(f"Error manually toggling light: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Start the sensor monitoring in a separate thread
    sensor_thread = threading.Thread(target=sensor_monitoring_wrapper)
    sensor_thread.daemon = True
    sensor_thread.start()

    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from lighting import update_stack, set_light_manually, get_light_status
from flask_cors import CORS
import threading
import logging
from sensors import monitor_sensors

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")  # Allow WebSocket connections from this origin

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize thread-safe variables
lock = threading.Lock()
light_status = False
people_count = 0

def sensor_monitoring_wrapper():
    """Wrapper for sensor monitoring that includes WebSocket updates."""
    global light_status, people_count
    logging.info("Starting sensor monitoring thread")
    for event in monitor_sensors():
        is_entry = event.get('is_entry')
        with lock:
            people_count = update_stack(is_entry)
            light_status = get_light_status()
        notify_clients()

def notify_clients():
    """Send real-time updates to connected WebSocket clients."""
    with lock:
        socketio.emit('status_update', {
            'light_status': light_status,
            'people_count': people_count
        })

@app.route('/update', methods=['POST'])
def update():
    global light_status, people_count
    try:
        data = request.json
        is_entry = data.get('is_entry')
        with lock:
            people_count = update_stack(is_entry)
            light_status = get_light_status()
        notify_clients()
        return jsonify({'status': 'success', 'people_count': people_count, 'light_status': light_status})
    except Exception as e:
        logging.error(f"Error updating light status: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
    global light_status, people_count
    with lock:
        return jsonify({'light_status': light_status, 'people_count': people_count})

@app.route('/manual-toggle', methods=['POST'])
def manual():
    global light_status
    try:
        data = request.json
        light_status = set_light_manually(data.get('light_status'))
        notify_clients()
        return jsonify({'status': 'success', 'light_status': light_status})
    except Exception as e:
        logging.error(f"Error manually toggling light: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Start the sensor monitoring in a separate thread
    sensor_thread = threading.Thread(target=sensor_monitoring_wrapper)
    sensor_thread.daemon = True
    sensor_thread.start()

    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
