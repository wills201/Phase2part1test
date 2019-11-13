# This function calculates the distance between the points 
import day24classwork.csv
def edistance(x1, x2):
    distance = 0
    for i in range(len(x1)):
        distance += (x1[i] - x2[i])
    return distance

data = day24classwork.csv
ndata = data[0]
#Compares all data to first data point
for row in data:
    distance = edistance(ndata, row)
#Gets similar neighbors
def neighbors(train, test_row, k):
	distances = list()
	for train_row in train:
		dist = edistance(test_row, train_row)
		distances.append((train_row, dist))
	neighbors = list()
    distances.sort()
	for i in range(k):
		neighbors.append(distances[i][0])
	return neighbors

def predictions()
    
