def set_up_pin(GPIO, sensor_1, sensor_2, sensor_3, sensor_4, sensor_5, enRight, enLeft, inRight1, inRight2, inLeft1,
               inLeft2):
    GPIO.setup(sensor_1, GPIO.IN)
    GPIO.setup(sensor_2, GPIO.IN)
    GPIO.setup(sensor_3, GPIO.IN)
    GPIO.setup(sensor_4, GPIO.IN)
    GPIO.setup(sensor_5, GPIO.IN)

    GPIO.setup(enRight, GPIO.OUT)
    GPIO.setup(enLeft, GPIO.OUT)

    GPIO.setup(inRight1, GPIO.OUT)
    GPIO.setup(inRight2, GPIO.OUT)

    GPIO.setup(inLeft1, GPIO.OUT)
    GPIO.setup(inLeft2, GPIO.OUT)

    GPIO.output(inRight1, GPIO.LOW)
    GPIO.output(inRight2, GPIO.LOW)
    GPIO.output(inLeft1, GPIO.LOW)
    GPIO.output(inLeft2, GPIO.LOW)
