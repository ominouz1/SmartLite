from flask import Flask, jsonify, request
from lighting import update_stack, set_light_manually, get_light_status
import threading
from sensors import monitor_sensors


app = Flask(__name__)


# Global variables to track the light status and people count
light_status = False  # False means lights off, True means lights on
people_count = 0


# Start the sensor monitoring in a separate thread
sensor_thread = threading.Thread(target=monitor_sensors, args=(app,))
sensor_thread.daemon = True
sensor_thread.start()


@app.route('/update', methods=['POST'])
def update():
    global light_status, people_count
    data = request.json
    is_entry = data.get('is_entry')
    people_count = update_stack(is_entry)
    light_status = get_light_status()
    return jsonify({'status': 'success', 'people_count': people_count, 'light_status': light_status})


@app.route('/status', methods=['GET'])
def status():
    global light_status, people_count
    return jsonify({'light_status': light_status, 'people_count': people_count})


@app.route('/manual', methods=['POST'])
def manual():
    global light_status
    data = request.json
    light_status = set_light_manually(data.get('light_status'))
    return jsonify({'status': 'success', 'light_status': light_status})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





