
"""
0,0
2,1
4,2
6,3
"""
import math
import numpy as np

def FindTrees(input_list, slope):
    count = 0
    for i, line in enumerate(input_list):
        j = slope * i
        if isinstance(slope, float):
            if not j.is_integer():
                continue
        if line[int(j)] == '#':
            count += 1
    return count


if __name__ == '__main__':
    # Read the input
    input_file = open('/Users/ambuj/Desktop/advent_of_code/data/day_3.txt', "r")
    input_strings = input_file.readlines()
    lines_list = [line.strip() for line in input_strings]

    # Find the number of times the pattern needs to be repeated
    depth = len(lines_list)
    print('The depth of the input is: {}'.format(depth))

    # Find width and the number of times the pattern needs to be repeated
    width = len(lines_list[0])
    print('The width of the input is: {}'.format(width))

    slopes = [1, 3, 5, 7, 0.5]
    tree_count_list = []
    for slope in slopes:
        num_repetitions = math.ceil(depth * slope / width)
        print('The pattern will be repeated {} times'.format(num_repetitions))
        print('The new width will be: {}'.format(num_repetitions * width))

        # Get new pattern
        new_input = [inp * num_repetitions for inp in lines_list]

        tree_count = FindTrees(new_input, slope)
        tree_count_list.append(tree_count)
        print('Number of trees encountered: {}'.format(tree_count))


    print(tree_count_list)
    print(np.prod(tree_count_list))
    # Find the number of trees encountered
