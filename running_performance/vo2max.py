from math import exp


def VO2Max(distance, time, digits=2):
    """
    Returns VO2Max in ml/kg/min
    """
    time /= 60
    velocity = distance / time

    percent_max = (
        0.8
        + 0.1894393 * exp(-0.012778 * time)
        + 0.2989558 * exp(-0.1932605 * time)
    )
    vo2 = -4.60 + 0.182258 * velocity + 0.000104 * velocity * velocity
    vo2max = vo2 / percent_max
    return round(vo2max, digits)
