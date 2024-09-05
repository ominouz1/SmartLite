import RPi.GPIO as GPIO
import time
import threading
from flask_socketio import SocketIO, emit

# Setup GPIO pins
TRIG = 23
ECHO = 24
LIGHT_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

THRESHOLD_DISTANCE = 50  # Distance in cm to detect presence
light_status = False  # Global variable to track the light status
lock = threading.Lock()

# Initialize socketio
socketio = SocketIO()

def get_distance():
    """Get the distance reading from the ultrasonic sensor."""
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound is 34300 cm/s
    return round(distance, 2)

def control_light():
    """Monitor the distance and control the light automatically based on threshold."""
    global light_status
    while True:
        distance = get_distance()
        print(f"Distance: {distance} cm")

        with lock:
            if distance <= THRESHOLD_DISTANCE and not light_status:
                GPIO.output(LIGHT_PIN, GPIO.HIGH)
                light_status = True
                print("Light ON")
                # Emit WebSocket event when the light is automatically turned on
                socketio.emit('status_update', {'light_status': True})
            elif distance > THRESHOLD_DISTANCE and light_status:
                GPIO.output(LIGHT_PIN, GPIO.LOW)
                light_status = False
                print("Light OFF")
                # Emit WebSocket event when the light is automatically turned off
                socketio.emit('status_update', {'light_status': False})

        time.sleep(1)

def manual_control(status):
    """Manually control the light based on the API call."""
    global light_status
    with lock:
        if status and not light_status:
            GPIO.output(LIGHT_PIN, GPIO.HIGH)
            light_status = True
            print("Light manually turned ON")
        elif not status and light_status:
            GPIO.output(LIGHT_PIN, GPIO.LOW)
            light_status = False
            print("Light manually turned OFF")
    return light_status

def get_light_status():
    """Return the current light status."""
    global light_status
    with lock:
        return light_status

def cleanup_gpio():
    """Cleanup GPIO pins when exiting."""
    GPIO.cleanup()

