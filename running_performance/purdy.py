from .exceptions import DistanceOutOfBoundsError

C_K1 = 0.0654
C_K2 = 0.00258
C_A = 85
C_B = 950

PORTUGESE_TABLE = (
    (40, 11),
    (50, 10.9960),
    (60, 10.9830),
    (70, 10.9620),
    (80, 10.934),
    (90, 10.9000),
    (100, 10.8600),
    (110, 10.8150),
    (120, 10.765),
    (130, 10.7110),
    (140, 10.6540),
    (150, 10.5940),
    (160, 10.531),
    (170, 10.4650),
    (180, 10.3960),
    (200, 10.2500),
    (220, 10.096),
    (240, 9.9350),
    (260, 9.7710),
    (280, 9.6100),
    (300, 9.455),
    (320, 9.3070),
    (340, 9.1660),
    (360, 9.0320),
    (380, 8.905),
    (400, 8.7850),
    (450, 8.5130),
    (500, 8.2790),
    (550, 8.083),
    (600, 7.9210),
    (700, 7.6690),
    (800, 7.4960),
    (900, 7.32000),
    (1000, 7.18933),
    (1200, 6.98066),
    (1500, 6.75319),
    (2000, 6.50015),
    (2500, 6.33424),
    (3000, 6.21913),
    (3500, 6.13510),
    (4000, 6.07040),
    (4500, 6.01822),
    (5000, 5.97432),
    (6000, 5.90181),
    (7000, 5.84156),
    (8000, 5.78889),
    (9000, 5.74211),
    (10000, 5.70050),
    (12000, 5.62944),
    (15000, 5.54300),
    (20000, 5.43785),
    (25000, 5.35842),
    (30000, 5.29298),
    (35000, 5.23538),
    (40000, 5.18263),
    (50000, 5.08615),
    (60000, 4.99762),
    (80000, 4.83617),
    (100000, 4.68988),
)


def _fraction_on_turns(distance):
    track_length = 400
    if distance < 110:
        return 0
    laps = int(distance / track_length)
    meters = distance % track_length

    if meters <= 50:
        part_lap = 0
    elif meters <= 150:
        part_lap = meters - 50
    elif meters <= 250:
        part_lap = 100
    elif meters <= 350:
        part_lap = 100 + (meters - 250)
    elif meters <= 400:
        part_lap = 200

    turn_distance = laps * 0.5 * track_length + part_lap
    return turn_distance / distance


def _interpolate(distance):
    c1 = 0.2
    c2 = 0.08
    c3 = 0.0065

    if distance < PORTUGESE_TABLE[0][0] or distance > PORTUGESE_TABLE[-1][0]:
        raise DistanceOutOfBoundsError()

    for index in range(len(PORTUGESE_TABLE)):
        if distance <= PORTUGESE_TABLE[index + 1][0]:
            lower_distance, lower_velocity = PORTUGESE_TABLE[index]
            upper_distance, upper_velocity = PORTUGESE_TABLE[index + 1]
            break
    lower_time = lower_distance / lower_velocity
    upper_time = upper_distance / upper_velocity

    time_interpolated = (
        lower_time +
        (upper_time - lower_time) * (distance - lower_distance) / (upper_distance - lower_distance)
    )
    velocity_interpolated = distance / time_interpolated

    time_950 = (
        time_interpolated
        + c1
        + c2 * velocity_interpolated
        + c3 * _fraction_on_turns(distance) * pow(velocity_interpolated, 2)
    )

    return velocity_interpolated, time_950


def purdy(distance, time, digits=2):
    """
    Returns Purdy Points based on Portugese Tables
    """

    velocity_interpolated, time_950 = _interpolate(distance)

    k = C_K1 - C_K2 * velocity_interpolated
    a = C_A / k
    b = 1 - C_B / a
    points = a * (time_950 / time - b)
    return points if digits is None else round(points, digits)


def purdy_prediction(distance, time, distance_to_predict):
    points = purdy(distance, time, digits=None)

    velocity_interpolated, time_950 = _interpolate(distance_to_predict)
    k = C_K1 - C_K2 * velocity_interpolated
    a = C_A / k
    b = 1 - C_B / a

    time_to_predict = time_950 / (points / a + b)
    return int(round(time_to_predict))
