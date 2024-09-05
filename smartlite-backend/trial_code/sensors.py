import RPi.GPIO as GPIO
import time


# Setup GPIO pins
TRIG = 23
ECHO = 24
LIGHT_PIN = 18


GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LIGHT_PIN, GPIO.OUT)


THRESHOLD_DISTANCE = 50  # Distance in cm to detect presence


def get_distance():
    # Send a 10us pulse to trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
   
    # Record the time when the pulse was sent
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
   
    # Record the time when the pulse is received back
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
   
    # Calculate the duration of the pulse
    pulse_duration = pulse_end - pulse_start
   
    # Convert pulse duration to distance
    distance = pulse_duration * 17150  # Speed of sound is 34300 cm/s
   
    return round(distance, 2)


def control_light():
    while True:
        distance = get_distance()
        print(f"Distance: {distance} cm")
       
        if distance <= THRESHOLD_DISTANCE:
            # Turn on the light
            GPIO.output(LIGHT_PIN, GPIO.HIGH)
            print("Light ON")
        else:
            # Turn off the light
            GPIO.output(LIGHT_PIN, GPIO.LOW)
            print("Light OFF")
       
        time.sleep(1)


try:
    control_light()
except KeyboardInterrupt:
    GPIO.cleanup()





