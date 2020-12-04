def SumOfNumbers2020(numbers_list):
    for first_number in numbers_list:
        for second_number in numbers_list:
            for third_number in numbers_list:
                if first_number + second_number + third_number == 2020:
                    return first_number, second_number, third_number

    return None


if __name__ == '__main__':
    # Read input file
    # Read a text file
    input_file = open('/Users/ambuj/Desktop/advent_of_code/data/day_1.txt', "r")
    input_strings = input_file.readlines()
    numbers = [int(num.strip()) for num in input_strings]

    first_number, second_number, third_number = SumOfNumbers2020(numbers)
    print('The two numbers are: {}, {} and {}'.format(first_number, second_number, third_number))
    print('Multiplication result is {}'.format(first_number*second_number*third_number))