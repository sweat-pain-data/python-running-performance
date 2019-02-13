import math
from running_performance import VO2Max, VO2Max_prediction


def test_VO2Max(performance):
    assert VO2Max(performance['distance'], performance['time']) == performance['VO2Max']


def test_VO2Max_time(VO2Max_time):
    prediction = VO2Max_prediction(VO2Max_time['distance'], VO2Max_time['time'], VO2Max_time['predicted_distance'])
    difference = prediction - VO2Max_time['predicted_time']
    assert math.fabs(difference) / VO2Max_time['predicted_time'] < 0.005
