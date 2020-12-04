from functools import reduce

open_space = '.'
tree = '#'

class Area:
    def __init__(self, matrix):
        self.height = len(matrix) - 1
        self.width = len(matrix[0]) - 1
        self.matrix = matrix
    
    def is_tree(self, position):
        if position[0] > self.height:
            return False
        row = self.matrix[position[0]]
        col = row[position[1] % (self.width+1)]
        return col == tree

def get_area():
    with open('3/3.input') as file:
        lines = file.read().strip().split('\n')
        return Area(lines)

# start in top left open space
# pattern repeates infinitly to the right so horizontal indexes use clock arithmetic
# a slope is a pair of integers (a, b) and is an integer vector
# for each tip of a vector count if there is a tree present

def count_trees(slope, area):
    curr_pos = (0, 0)
    tree_count = 0
    while curr_pos[0] <= area.height:
        curr_pos = tuple(i + j for i, j in zip(curr_pos, slope))
        if area.is_tree(curr_pos):
            tree_count += 1
    return tree_count


slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)] # down, right
area = get_area()
counts = map(lambda x : count_trees(x, area), slopes)
print(reduce(lambda accum, i : accum * i, counts))