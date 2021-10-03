def follow_line(sign_1, sign_2, sign_3, sign_4, sign_5):
    if sign_1 == 1 and sign_2 == 1 and sign_3 == 0 and sign_4 == 1 and sign_5 == 1:
        flag_sensor_light = "C"
        return flag_sensor_light
    elif sign_1 == 1 and sign_2 == 0 and sign_4 == 1 and sign_5 == 1:
        flag_sensor_light = "L"
        return flag_sensor_light
    elif sign_1 == 0 and sign_3 == 1 and sign_4 == 1 and sign_5 == 1:
        flag_sensor_light = "LM"
        return flag_sensor_light
    elif sign_1 == 1 and sign_2 == 1 and sign_4 == 0 and sign_5 == 1:
        flag_sensor_light = "R"
        return flag_sensor_light
    elif sign_1 == 1 and sign_2 == 1 and sign_3 == 1 and sign_5 == 0:
        flag_sensor_light = "RM"
        return flag_sensor_light
    elif sign_1 == 0 and sign_2 == 0 and sign_3 == 0 and sign_4 == 1 and sign_5 == 1:
        flag_sensor_light = "SOS"
        return flag_sensor_light
    elif sign_1 == 0 and sign_2 == 0 and sign_3 == 0 and sign_4 == 0 and sign_5 == 0:
        flag_sensor_light = "SOS"
        return flag_sensor_light
