# Initialize an array containing the robot's location belief function.
p = [0, 1, 0, 0, 0]

world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']

# Sensor accuracy
pHit = 0.6
pMiss = 0.2

# Movement accuracy
pExact = 0.8
pUndershoot = 0.1
pOvershoot = 0.1


def sense(belief_function: [int], measurement: str) -> [int]:
    """
    Produce a belief function based on a measurement.

    :param belief_function:
    :param measurement:
    :return:
    """

    q = []
    for i in range(len(belief_function)):
        hit = (measurement == world[i])
    q.append(belief_function[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


def move(belief_function: [int], movement: int) -> [int]:
    """
    Produce a belief function based on a movement.

    :param belief_function:
    :param movement:
    :return:
    """
    q = []
    for i in range(len(belief_function)):
        q.append(belief_function[i - movement] * pExact
                 + belief_function[i - (movement + 1)] * pOvershoot
                 + belief_function[i - (movement - 1)] * pUndershoot)
    return q


# Move twice
p = (move(move(p, 1), 1))

print(move(p, 1))