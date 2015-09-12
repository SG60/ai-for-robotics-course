# Initialize an empty array for the robot's location belief function
p = [0.2, 0.2, 0.2, 0.2, 0.2]
# Initialize world
world = ['green', 'red', 'red', 'green', 'green']
# Sensor result
Z = 'red'
# Sensor reliabilities
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    q = []

    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))

    a = sum(q)

    for i in range(len(p)):
        q[i] = q[i] / a

    return q


print(sense(p, Z))
