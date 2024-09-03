from flask import Flask, jsonify, request
from lighting import update_stack
import threading
from sensors import monitor_sensors

app = Flask(__name__)

# Start the sensor monitoring in a separate thread
sensor_thread = threading.Thread(target=monitor_sensors)
sensor_thread.daemon = True
sensor_thread.start()

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    is_entry = data.get('is_entry')
    people_count = update_stack(is_entry)
    return jsonify({'status': 'success', 'people_count': people_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
