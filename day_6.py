def ReadInputData(file_path):
    input_data = open(file_path, "r")
    input_strings = input_data.readlines()
    lines_list = [line.strip('\n\n') for line in input_strings]
    return lines_list


def GroupAnswersPerGroup(input_data):
    group_answers = []
    final_data = []
    for data in input_data:
        if data == "":
            final_data.append(group_answers)
            group_answers = []
        else:
            group_answers.append(data)
    return final_data


def NumDifferentAnswers(input_data_per_group):
    combined_data_per_group = "".join(input_data_per_group)
    return len(set(combined_data_per_group))


def NumSameAnserPerGroup(input_data_per_group):
    input_data_as_sets = [set(data) for data in input_data_per_group]
    return len(set.intersection(*input_data_as_sets))


if __name__ == '__main__':
    # Read Input
    input_data = ReadInputData('/Users/ambuj/Desktop/advent_of_code/data/day_6.txt')
    preprocessed_data = GroupAnswersPerGroup(input_data)

    num_answer_per_group = [NumDifferentAnswers(data) for data in preprocessed_data]
    print(sum(num_answer_per_group))

    same_answer_per_group = [NumSameAnserPerGroup(data) for data in preprocessed_data]
    print("Answer for part 2: {}".format(sum(same_answer_per_group)))
