##
##  basicBeliefArrayUpdater.py
##
##  A basic program that updates a location belief array for a simple
##  robot in a simple world...
##
##  copyright © Sam Greening 2014
##
#######################################################################

# Initialize an array for the robot's location belief function in a
# state of maximum confusion
p = [0.2, 0.2, 0.2, 0.2, 0.2]
# Initialize world
world = ['green', 'red', 'red', 'green', 'green']
# Sensor result array
measurements = ['red']
# Sensor reliabilities since sensing is not perfect
pHit = 0.6
pMiss = 0.2
# Movement reliabilities
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

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

def move(p, U):
	q = []
	for i in range(len(p)):
		q.append(p[i - U] * pExact + p[i - (U + 1)] * pOvershoot + p[i - (U - 1)] * pUndershoot)
	return q

for i in measurements:
	p = sense(p, i)

p = move(p, 1)

print p