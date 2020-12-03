# Load map.

with open('input', 'r') as f:
    forest_map = f.read().splitlines()

forest_map = [list(elem) for elem in forest_map]

# Get length of each line:
lenght = len(forest_map[0])

# The route is 3 right 1 down. So the elements that form the path are:
# Notice the first line is actually line 0.
# Line 1 -> elem 3
# Line 2 -> elem 6
#        ...
# Line n -> elem 3 * n

# An array is built with the characters in "elem" positions of each line.
# Due to periodic conditions, the index we actually need is the modulus of
# elem / lenght
path = [ forest_map[i][3*i % lenght] for i in range(1,len(forest_map))]

# Count number of trees in path (# character):
ntrees = path.count('#')

print('Number of trees:', ntrees)
