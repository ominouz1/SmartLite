import RPi.GPIO as GPIO

LIGHT_PIN = 17  # GPIO pin to control the light
GPIO.setup(LIGHT_PIN, GPIO.OUT)

stack = []

def turn_on_light():
    GPIO.output(LIGHT_PIN, True)

def turn_off_light():
    GPIO.output(LIGHT_PIN, False)

def update_stack(is_entry):
    global stack
    if is_entry:
        stack.append(1)
        if len(stack) == 1:
            turn_on_light()
    else:
        if stack:
            stack.pop()
            if not stack:
                turn_off_light()

    return len(stack)
