import RPi.GPIO as GPIO
import atexit
import logging

# Define the GPIO pin for the light
LIGHT_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

is_manual = None

light_status = False

# Initialize an empty stack
people_count = 0

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def turn_on_light():
    global light_status
    GPIO.output(LIGHT_PIN, GPIO.HIGH)
    light_status = True  # Light is ON
    logging.info("Light turned ON")

def turn_off_light():
    global light_status
    GPIO.output(LIGHT_PIN, GPIO.LOW)
    light_status = False  # Light is OFF
    logging.info("Light turned OFF")

def get_light_status():
    return light_status

def get_method():
    return is_manual

def update_people_count(is_entry):
    global people_count
    global is_manual
    if is_entry:
        people_count += 1
        logging.info(f"Person entered, people count: {people_count}")
        if people_count >= 1:  # Turn on the light when the first person enters
            if not light_status:
                turn_on_light()
                is_manual = False
    else:
        if people_count > 0:
            people_count -= 1
            logging.info(f"Person exited, people count: {people_count}")
            if people_count == 0:  # Turn off the light when the last person exits
                turn_off_light()
    return people_count

def set_light_manually(status):
    global is_manual
    if status:
        turn_on_light()
        is_manual = True
    else:
        turn_off_light()
        is_manual = True
    return get_light_status()

# Cleanup GPIO on exit
atexit.register(GPIO.cleanup)
