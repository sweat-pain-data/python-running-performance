import math
from running_performance import riegel_prediction


def test_riegel_time(riegel_time):
    prediction = riegel_prediction(riegel_time['distance'], riegel_time['time'], riegel_time['predicted_distance'])
    difference = prediction - riegel_time['predicted_time']
    assert math.fabs(difference) / riegel_time['predicted_time'] < 0.005
