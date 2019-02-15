def cameron_prediction(distance, time, distance_to_predict):
    a = 13.49681 - (0.000030363 * distance) + (835.7114 / (pow(distance, 0.7905)))
    b = 13.49681 - (0.000030363 * distance_to_predict) + (835.7114 / (pow(distance_to_predict, 0.7905)))
    time_to_predict = (time / distance) * (a / b) * distance_to_predict

    return time_to_predict
