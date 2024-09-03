import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG1 = 23  # GPIO pin for Sensor 1 TRIG
ECHO1 = 24  # GPIO pin for Sensor 1 ECHO
TRIG2 = 27  # GPIO pin for Sensor 2 TRIG
ECHO2 = 22  # GPIO pin for Sensor 2 ECHO

GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)

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
    
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    
    return distance

def monitor_sensors():
    while True:
        distance1 = get_distance(TRIG1, ECHO1)
        distance2 = get_distance(TRIG2, ECHO2)
        print(f"Distance1: {distance1} cm, Distance2: {distance2} cm")
        # Add logic here to push updates to the Flask app.
        time.sleep(1)
