import RPi.GPIO as GPIO
import time
import requests


# Setup GPIO Mode
GPIO.setmode(GPIO.BCM)


# Define GPIO Pins for Sensors
TRIG1 = 23  # Sensor 1 TRIG (Outside)
ECHO1 = 24  # Sensor 1 ECHO (Outside)
TRIG2 = 27  # Sensor 2 TRIG (Inside)
ECHO2 = 22  # Sensor 2 ECHO (Inside)


# Setup GPIO Pins
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)


# Global state to keep track of the last sensor activation
last_trigger = None
last_trigger_time = None


def get_distance(trig, echo):
    # Trigger the ultrasonic burst
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)


    # Measure the echo return time
    start_time = time.time()
    stop_time = time.time()


    while GPIO.input(echo) == 0:
        start_time = time.time()


    while GPIO.input(echo) == 1:
        stop_time = time.time()


    # Calculate the distance based on the time
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # Speed of sound in cm/s


    return distance


def monitor_sensors(app):
    global last_trigger, last_trigger_time
    threshold_distance = 100  # Adjust as needed


    with app.app_context():
        while True:
            distance1 = get_distance(TRIG1, ECHO1)
            distance2 = get_distance(TRIG2, ECHO2)
            print(f"Distance1: {distance1} cm, Distance2: {distance2} cm")


            if distance1 < threshold_distance and (last_trigger != 'TRIG1' or time.time() - last_trigger_time > 2):
                # Sensor 1 (outside) triggered
                last_trigger = 'TRIG1'
                last_trigger_time = time.time()


            if distance2 < threshold_distance and last_trigger == 'TRIG1' and time.time() - last_trigger_time < 2:
                # Sensor 2 (inside) triggered after Sensor 1, hence someone entered
                requests.post('http://127.0.0.1:5000/update', json={'is_entry': True})
                last_trigger = 'TRIG2'
                last_trigger_time = time.time()


            if distance2 < threshold_distance and (last_trigger != 'TRIG2' or time.time() - last_trigger_time > 2):
                # Sensor 2 (inside) triggered
                last_trigger = 'TRIG2'
                last_trigger_time = time.time()


            if distance1 < threshold_distance and last_trigger == 'TRIG2' and time.time() - last_trigger_time < 2:
                # Sensor 1 (outside) triggered after Sensor 2, hence someone exited
                requests.post('http://127.0.0.1:5000/update', json={'is_entry': False})
                last_trigger = 'TRIG1'
                last_trigger_time = time.time()


            time.sleep(0.1)  







