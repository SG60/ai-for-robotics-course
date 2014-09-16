# Initialize an empty array for the robot's location belief function
p = [0.2, 0.2, 0.2, 0.2, 0.2]
# Initialize world
world = ['green', 'red', 'red', 'green', 'green']
# Sensor result array
measurements = ['red', 'green']
# Sensor reliabilities
pHit = 0.6
pMiss = 0.2

def sense(p, Z):

	q = []

	for i in range(len(p)):

		# Set hit to 1 if Z equals world[i] tile colour, else Z = 0
		hit = (Z == world[i])

		# Append a belief to q for each tile. If hit == 1, then
		# q[i]=p[i]*pHit, else q[i]=p[i]*pMiss
		q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))

	a = sum(q)

	# Normalize the values of q so they sum(q)==1
	for i in range(len(p)):
		q[i] = q[i]/a

	return q

for k in range(len(measurements)):
	p = sense(p, k)

print p