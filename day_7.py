from collections import defaultdict


class Node:
    def __init__(self, id):
        self.id = id


def ReadInput(file_path):
    input_data = open(file_path, "r")
    input_strings = input_data.readlines()
    lines_list = [line.strip() for line in input_strings]
    return lines_list


def ParseStringToDict(rules_list):
    rule_as_dict = {}

    for rule in rules_list:
        outer_bag = rule[:rule.find('bags')].strip()
        rule_as_dict[outer_bag] = {}
        num_inner_bags = rule.count(',') + 1

        inner_bags_substring = rule[rule.find('contain') + len('contain') + 1:].strip()
        for i in range(num_inner_bags):
            for char_index, letter in enumerate(inner_bags_substring):
                if letter.isdigit():
                    num_bag = int(letter)
                    if num_bag == 1:
                        bag_color = inner_bags_substring[inner_bags_substring.find(letter) + 1:inner_bags_substring.find('bag')].strip()
                        inner_bags_substring = inner_bags_substring[inner_bags_substring.find(letter) + 1:].strip()
                        inner_bags_substring = inner_bags_substring[inner_bags_substring.find(bag_color) + len(bag_color) + len('bag') + 1:].strip()
                    else:
                        bag_color = inner_bags_substring[inner_bags_substring.find(letter) + 1:inner_bags_substring.find('bags')].strip()
                        inner_bags_substring = inner_bags_substring[inner_bags_substring.find(letter) + 1:].strip()
                        inner_bags_substring = inner_bags_substring[inner_bags_substring.find(bag_color) + len(bag_color) + len('bags') + 1:].strip()
                    rule_as_dict[outer_bag].update({bag_color:num_bag})
                    break

    return rule_as_dict


def SolutionPart1(bags, searching_for='shiny gold'):
    inside = []
    try:
        for parent, contains in bags.items():
            if searching_for in contains.keys():
                inside.append(parent)
                inside.extend(SolutionPart1(bags, parent))
    except:
        return []
    return inside


def SolutionPart2(bags, searching_for='shiny gold'):
    bag_count = 1
    for parent, contains in bags[searching_for].items():
        bag_count += contains * SolutionPart2(bags, parent)
    return bag_count


if __name__ == '__main__':
    # Read the input
    rules_list = ReadInput('/Users/ambuj/Desktop/advent_of_code/data/day_7.txt')

    rules_dict = ParseStringToDict(rules_list)

    part_1_ans = SolutionPart1(rules_dict)
    print('Part 1 answer: {}'.format(len(set(part_1_ans))))

    total_bags = SolutionPart2(rules_dict)
    print('Part 2 answer: {}'.format(total_bags - 1))
