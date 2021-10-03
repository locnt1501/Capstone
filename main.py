import cv2
import RPi.GPIO as GPIO
from detect_villa import detect_villa
from gpiozero import DistanceSensor
from car_speed import stop, forward_with_speed, turn_right, turn_right_max, turn_left, turn_left_max, turn_left_max_sos
from detect_line import follow_line
from detect_traffic_sign import detect_traffic_sign
from set_up_pin import set_up_pin

enRight = 12
enLeft = 13

inRight1 = 17
inRight2 = 27

inLeft1 = 22
inLeft2 = 23

sensor_1 = 16
sensor_2 = 20
sensor_3 = 21
sensor_4 = 6
sensor_5 = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# setup pin on PI
set_up_pin(GPIO, sensor_1, sensor_2, sensor_3, sensor_4, sensor_5, enRight, enLeft, inRight1, inRight2, inLeft1,
           inLeft2)
frequency = 1000
speed = 100
runLeft = GPIO.PWM(enLeft, frequency)
runRight = GPIO.PWM(enRight, frequency)
runLeft.start(speed)
runRight.start(speed)
cap = cv2.VideoCapture(0)
# end setup Pi

# start variable
flag_prioritize = 0
detect = None
flag_sensor_light = "C"
flag_detect_traffic_sign = 0
value_traffic_sign = ''
villa_name = ''
sensor = DistanceSensor(echo=18, trigger=24, max_distance=5)
# end variable
array = [
    {"left": "HOME"},
    {"right": "P1"},
    {"forward": "SONA"},
    {"right": "P2"},
    {"stop": "NAMI"}
]
while True:
    ret, frame = cap.read()
    key = cv2.waitKey(1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Camera Car", frame)
    while sensor.distance * 100 < 20:
        print("DUng lai")
        stop()
    forward_with_speed(speed, runLeft, runRight, GPIO, inRight1, inRight2, inLeft1, inLeft2)
    sign_1 = GPIO.input(sensor_1)
    sign_2 = GPIO.input(sensor_2)
    sign_3 = GPIO.input(sensor_3)
    sign_4 = GPIO.input(sensor_4)
    sign_5 = GPIO.input(sensor_5)
    flag_sensor_light = follow_line(sign_1, sign_2, sign_3, sign_4, sign_5)
    if flag_sensor_light == "C":
        forward_with_speed(speed, runLeft, runRight, GPIO, inRight1, inRight2, inLeft1, inLeft2)
    elif flag_sensor_light == "R":
        turn_right(10, runRight, GPIO, inRight1, inRight2, inLeft1, inLeft2)
    elif flag_sensor_light == "RM":
        turn_right_max(inRight1, inRight2, inLeft1, inLeft2, GPIO)
    elif flag_sensor_light == "L":
        turn_left(10, runLeft, GPIO, inRight1, inRight2, inLeft1, inLeft2)
    elif flag_sensor_light == "LM":
        turn_left_max(inRight1, inRight2, inLeft1, inLeft2, GPIO)
    elif flag_sensor_light == "SOS":
        if flag_detect_traffic_sign == 1:
            while value_traffic_sign == "LEFT":
                turn_left_max_sos(runLeft, runRight, GPIO, inRight1, inRight2, inLeft1, inLeft2)
                sign_1 = GPIO.input(sensor_1)
                sign_2 = GPIO.input(sensor_2)
                sign_3 = GPIO.input(sensor_3)
                sign_4 = GPIO.input(sensor_4)
                sign_5 = GPIO.input(sensor_5)
                if sign_1 == 0 and sign_2 == 0 and sign_3 == 1 and sign_4 == 1 and sign_5 == 1:
                    # return init value
                    flag_detect_traffic_sign = 0
                    value_traffic_sign = ''
    # detect traffic sign
    value = detect_traffic_sign(cv2, gray)
    if value is not None:
        flag_detect_traffic_sign = 1
        value_traffic_sign = value

    # detect villa
    villa_name = detect_villa(frame)
    print(villa_name)
    if (key == ord('q')):
        break
GPIO.output(inRight1, GPIO.LOW)
GPIO.output(inRight2, GPIO.LOW)
GPIO.output(inLeft1, GPIO.LOW)
GPIO.output(inLeft2, GPIO.LOW)
cap.release()
cv2.destroyAllWindows()
