def riegel_prediction(distance, time, distance_to_predict):
    time = time * pow(distance_to_predict / distance, 1.06)
    return time
