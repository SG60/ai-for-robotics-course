# Initialize an empty array for the robot's location belief function
p = []
# Number of possible locations it could be at
n = 5

# Initialize all locations as equally probable
for i in range(n):
	p.append(1./n)

print(p)