# Load map.

with open('input', 'r') as f:
    forest_map = f.read().splitlines()

forest_map = [list(elem) for elem in forest_map]

# Get length of each line:
lenght = len(forest_map[0])

routes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

# The route is nright right and ndown down. So the elements that form the path are:

# An array is built with the characters in "elem" positions of each line.
# Due to periodic conditions, the index we actually need is the modulus of
# elem / lenght

tree_prod = 1
for route in routes:
    nright, ndown = route[0], route[1]
    path = [ forest_map[i*ndown][nright*i % lenght] for i in range(1,int(len(forest_map)/ndown))]

    # Count number of trees in path (# character):
    ntrees = path.count('#')

    # Multiply the number of trees:
    tree_prod *= ntrees

    print('Route', route)
    print('Number of trees:', ntrees)

print('Tree product:', tree_prod)
