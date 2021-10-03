def forward_with_speed(speed, runLeft, runRight, GPIO, inRight1, inRight2, inLeft1, inLeft2):
    runLeft.ChangeDutyCycle(speed)
    runRight.ChangeDutyCycle(speed)
    GPIO.output(inRight1, GPIO.LOW)
    GPIO.output(inRight2, GPIO.HIGH)
    GPIO.output(inLeft1, GPIO.LOW)
    GPIO.output(inLeft2, GPIO.HIGH)


def turn_left(turn_value, runLeft, GPIO, inRight1, inRight2, inLeft1, inLeft2):
    runLeft.ChangeDutyCycle(turn_value)
    GPIO.output(inRight1, GPIO.LOW)
    GPIO.output(inRight2, GPIO.HIGH)
    GPIO.output(inLeft1, GPIO.LOW)
    GPIO.output(inLeft2, GPIO.LOW)


def turn_right(turn_value, runRight, GPIO, inRight1, inRight2, inLeft1, inLeft2):
    runRight.ChangeDutyCycle(turn_value)
    GPIO.output(inRight1, GPIO.LOW)
    GPIO.output(inRight2, GPIO.LOW)
    GPIO.output(inLeft1, GPIO.LOW)
    GPIO.output(inLeft2, GPIO.HIGH)


def turn_left_max(inRight1, inRight2, inLeft1, inLeft2, GPIO):
    GPIO.output(inRight1, GPIO.LOW)
    GPIO.output(inRight2, GPIO.HIGH)
    GPIO.output(inLeft1, GPIO.LOW)
    GPIO.output(inLeft2, GPIO.LOW)


def turn_right_max(inRight1, inRight2, inLeft1, inLeft2, GPIO):
    GPIO.output(inRight1, GPIO.LOW)
    GPIO.output(inRight2, GPIO.LOW)
    GPIO.output(inLeft1, GPIO.LOW)
    GPIO.output(inLeft2, GPIO.HIGH)


def turn_left_max_sos(runLeft, runRight, GPIO, inRight1, inRight2, inLeft1, inLeft2):
    runLeft.ChangeDutyCycle(50)
    runRight.ChangeDutyCycle(50)
    GPIO.output(inRight1, GPIO.LOW)
    GPIO.output(inRight2, GPIO.HIGH)
    GPIO.output(inLeft1, GPIO.HIGH)
    GPIO.output(inLeft2, GPIO.LOW)


def turn_right_max_sos(runLeft, runRight, GPIO, inRight1, inRight2, inLeft1, inLeft2):
    runLeft.ChangeDutyCycle(50)
    runRight.ChangeDutyCycle(50)
    GPIO.output(inRight1, GPIO.HIGH)
    GPIO.output(inRight2, GPIO.LOW)
    GPIO.output(inLeft1, GPIO.LOW)
    GPIO.output(inLeft2, GPIO.HIGH)


def stop(GPIO, inRight1, inRight2, inLeft1, inLeft2):
    GPIO.output(inRight1, GPIO.LOW)
    GPIO.output(inRight2, GPIO.LOW)
    GPIO.output(inLeft1, GPIO.LOW)
    GPIO.output(inLeft2, GPIO.LOW)
