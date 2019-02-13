from math import exp, fabs

C1 = 0.8
C2 = 0.1894393
C3 = -0.012778
C4 = 0.2989558
C5 = -0.1932605
C6 = -4.60
C7 = 0.182258
C8 = 0.000104


def _percent_max(time_min):
    return C1 + C2 * exp(C3 * time_min) + C4 * exp(C5 * time_min)


def _percent_max_prime(time_min):
    return C2 * C3 * exp(C3 * time_min) + C4 * C5 * exp(C5 * time_min)


def _vo2(distance, time_min):
    velocity = distance / time_min
    return C6 + C7 * velocity + C8 * velocity**2


def _vo2_prime(distance, time_min):
    return -(C7 * distance / time_min**2) - (2 * C8 * distance**2 / time_min**3)


def VO2Max(distance, time, digits=2):
    """
    Returns VO2Max in ml/kg/min
    """
    time /= 60
    percent_max = _percent_max(time)
    vo2 = _vo2(distance, time)
    vo2max = vo2 / percent_max
    return vo2max if digits is None else round(vo2max, digits)


def _VO2Max_prime(distance, time_min):
    v = _vo2(distance, time_min)
    v_prime = _vo2_prime(distance, time_min)
    p = _percent_max(time_min)
    p_prime = _percent_max_prime(time_min)

    return (v_prime * p - v * p_prime) / p**2


def VO2Max_prediction(distance, time, distance_to_predict):
    VO2Max_achieved = VO2Max(distance, time, None)
    epsilon = 1 / 100 / 100
    predicted_time = time * distance_to_predict / distance

    while True:
        VO2Max_predicted = VO2Max(distance_to_predict, predicted_time)
        difference = fabs(VO2Max_predicted - VO2Max_achieved) / VO2Max_achieved
        if difference <= epsilon:
            break

        VO2Max_predicted_prime = _VO2Max_prime(distance_to_predict, predicted_time / 60)
        predicted_time -= (VO2Max_predicted - VO2Max_achieved) / VO2Max_predicted_prime

    return int(round(predicted_time, 0))
