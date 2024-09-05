import RPi.GPIO as GPIO
import time
import logging

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

# Global state for sensor sequence tracking
state = 'IDLE'
last_trigger_time = None
event = None

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def get_distance(trig, echo):
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(echo) == 0:
        start_time = time.time()

    while GPIO.input(echo) == 1:
        stop_time = time.time()

    # Calculate distance
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # Speed of sound in cm/s
    return distance

def monitor_sensors():
    global state, last_trigger_time, event
    threshold_distance = 50  # Adjust distance threshold
    timeout = 2  # Maximum allowed time between sensor activations (seconds)

    try:
        while True:
            distance1 = get_distance(TRIG1, ECHO1)  # Outside sensor
            distance2 = get_distance(TRIG2, ECHO2)  # Inside sensor
            current_time = time.time()

            logging.info(f"Distance1 (Outside): {distance1} cm, Distance2 (Inside): {distance2} cm")
            logging.info(f"Current state: {state}")

            # State machine for detecting entry and exit
            if state == 'IDLE':
                if distance1 < threshold_distance:
                    state = 'TRIG1_DETECTED'
                    last_trigger_time = current_time
                    logging.info("Person detected near outside sensor - possible entry")
                elif distance2 < threshold_distance:
                    state = 'TRIG2_DETECTED'
                    last_trigger_time = current_time
                    logging.info("Person detected near inside sensor - possible exit")

            elif state == 'TRIG1_DETECTED':  # Possible entry
                if distance2 < threshold_distance and (current_time - last_trigger_time) < timeout:
                    event = {'is_entry': True}
                    state = 'IDLE'
                    logging.info("Person confirmed entry")
                    yield event
                elif (current_time - last_trigger_time) >= timeout:
                    state = 'IDLE'  # Timeout, reset state

            elif state == 'TRIG2_DETECTED':  # Possible exit
                if distance1 < threshold_distance and (current_time - last_trigger_time) < timeout:
                    event = {'is_entry': False}
                    state = 'IDLE'
                    logging.info("Person confirmed exit")
                    yield event
                elif (current_time - last_trigger_time) >= timeout:
                    state = 'IDLE'  # Timeout, reset state

            time.sleep(0.1)

    except Exception as e:
        logging.error(f"Error in sensor monitoring: {e}")
    finally:
        pass
