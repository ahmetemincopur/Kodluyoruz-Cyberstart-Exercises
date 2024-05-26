import math

# Step 1: Define the points
points = [
    (1, 2),
    (4, 6),
    (5, 8),
    (1, 7),
    (2, 3)
]

# Step 2: Write the Euclidean distance function
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Step 3: Calculate distances using a loop
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Step 4: Find the minimum distance
min_distance = min(distances)
print(f"The minimum distance is: {min_distance}")
