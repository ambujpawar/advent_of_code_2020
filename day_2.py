sample_input = '1-4 j: jjjqzmgbjwpj'


def GetNumbers(sample_input):
    return sample_input.split()[0]


def GetLetterOfInterest(sample_input):
    return sample_input[0]


def ExtractInfoFromString(sample_input):
    string_splitter = sample_input.split()
    #assert(len(string_splitter) == 3, 'There should be just 2 spaces in the input')

    # Get min max numbers
    numbers = GetNumbers(string_splitter[0])
    occurences = [int(s) for s in numbers.split('-') if s.isdigit()]
    #assert(len(occurences) == 2, 'Only 2 numbers expected. Got {}'.format(len(occurences)))

    # Get Letter
    letter = GetLetterOfInterest(string_splitter[1])

    # Get Password
    password = string_splitter[2]
    return occurences[0], occurences[1], letter, password


def IsPasswordCorrect(password, letter, min_occurence, max_occurence):
    occurence_in_str = 0

    for s in password:
        if s==letter:
            occurence_in_str += 1

    if min_occurence <= occurence_in_str <= max_occurence:
        return True
    else:
        return False


def IsPasswordCorrectNew(password, letter, first_occurence, second_occurence):
    # To make it compatile as index starts from 1 in the file
    first_occurence = first_occurence - 1
    second_occurence = second_occurence - 1
    if password[first_occurence] == letter and password[second_occurence] != letter:
        return True
    elif password[first_occurence] != letter and password[second_occurence] == letter:
        return True
    else:
        return False


if __name__ == '__main__':

    # Read a text file
    input_file = open('/Users/ambuj/Desktop/advent_of_code/data/input_day_2.txt', "r")
    input_strings = input_file.readlines()

    correct_passwords = 0
    for sample_case in input_strings:
        # Read atleast- atmost numbers
        input_str = sample_case.strip()
        min_occurence, max_occurence, letter, password = ExtractInfoFromString(input_str)
        is_password_correct = IsPasswordCorrectNew(password, letter, min_occurence, max_occurence)

        if is_password_correct:
            correct_passwords += 1

    print('Number of correct passwords: {}'.format(correct_passwords))
