# Initialize an array containing the robot's location belief function.
p = [0.2, 0.2, 0.2, 0.2, 0.2]

world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1, 1]

# Sensor accuracy
pHit = 0.6
pMiss = 0.2

# Movement accuracy
pExact = 0.8
pUndershoot = 0.1
pOvershoot = 0.1


def sense(belief_function, measurement):
    """
    Produce a belief function based on a measurement.

    :type belief_function: list[int]
    :type measurement: str
    :rtype : list[int]
    """

    q = []
    for i in range(len(belief_function)):
        hit = (measurement == world[i])
        q.append(belief_function[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    q = [i / s for i in q]
    return q


def move(belief_function, movement):
    """
    Produce a belief function based on a movement.

    :type belief_function: list[int]
    :type movement: int
    :rtype : list[int]
    """
    q = []
    for i in range(len(belief_function)):
        q.append(belief_function[i - movement] * pExact
                 + belief_function[(i - (movement + 1)) % len(belief_function)] * pOvershoot
                 + belief_function[(i - (movement - 1)) % len(belief_function)] * pUndershoot)
    return q


# Move robot
for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])

print p
