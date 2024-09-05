import RPi.GPIO as GPIO
import atexit

# Define the GPIO pin for the light
LIGHT_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

light_status = False

# Initialize an empty stack
stack = []

def turn_on_light():
    global light_status
    GPIO.output(LIGHT_PIN, GPIO.HIGH)
    light_status = True  # Light is ON

def turn_off_light():
    global light_status
    GPIO.output(LIGHT_PIN, GPIO.LOW)
    light_status = False  # Light is OFF

def get_light_status():
    return light_status

def update_stack(is_entry):
    global stack
    if is_entry:
        stack.append(1)
        if len(stack) >= 1:  # Turn on the light when the first person enters
            turn_on_light()
    else:
        if stack:
            stack.pop()
            if not stack:  # Turn off the light when the last person exits
                turn_off_light()
    return len(stack)

def set_light_manually(status):
    if status:
        turn_on_light()
    else:
        turn_off_light()
    return get_light_status()

# Cleanup GPIO on exit
atexit.register(GPIO.cleanup)
import RPi.GPIO as GPIO
import atexit

# Define the GPIO pin for the light
LIGHT_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

light_status = False

# Initialize an empty stack
stack = []

def turn_on_light():
    global light_status
    GPIO.output(LIGHT_PIN, GPIO.HIGH)
    light_status = True  # Light is ON

def turn_off_light():
    global light_status
    GPIO.output(LIGHT_PIN, GPIO.LOW)
    light_status = False  # Light is OFF

def get_light_status():
    return light_status

def update_stack(is_entry):
    global stack
    if is_entry:
        stack.append(1)
        if len(stack) >= 1:  # Turn on the light when the first person enters
            turn_on_light()
    else:
        if stack:
            stack.pop()
            if not stack:  # Turn off the light when the last person exits
                turn_off_light()
    return len(stack)

def set_light_manually(status):
    if status:
        turn_on_light()
    else:
        turn_off_light()
    return get_light_status()

# Cleanup GPIO on exit
atexit.register(GPIO.cleanup)
