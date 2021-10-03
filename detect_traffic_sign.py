def detect_traffic_sign(cv2, gray):
    # detect traffic sign
    detect_right = cv2.CascadeClassifier('data_traffic_signs/right.xml')
    detect_left = cv2.CascadeClassifier('data_traffic_signs/left.xml')
    detect_stop = cv2.CascadeClassifier('data_traffic_signs/stop.xml')
    array = {
        'STOP': detect_stop,
        'RIGHT': detect_right,
        'LEFT': detect_left
    }
    for k, v in array.items():
        detect = v.detectMultiScale(gray, 1.9, 7)
        if type(detect) != tuple:
            return k
