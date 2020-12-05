"""
Solution to day 5 of advent of code 2020
Read the boarding passes problem
The boarding passes letters seems to arranged in a binary format
The first seven digit[0-6] represent rows and the remaining 3 digits[7-9] represent column
"""
TEST_STRINGS = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']


def ReadInputData(file_path):
    input_data = open(file_path, "r")
    input_strings = input_data.readlines()
    lines_list = [line.strip() for line in input_strings]
    return lines_list


def ConvertPasscodeToSeatNumber(string):
    binary_passcode = string.replace("R", "1").replace("L", "0").replace("B", "1").replace("F", "0")
    seat_number = int(binary_passcode, 2)
    return seat_number


def FindMissingSeat(seat_numbers):
    min_seat_num = min(seat_numbers)
    max_seat_num = max(seat_numbers)
    for x in range(min_seat_num, max_seat_num):
        if x not in seat_numbers:
            return x

    return None


if __name__ == '__main__':
    # Read the input
    input_passcodes = ReadInputData('/Users/ambuj/Desktop/advent_of_code/data/day_5.txt')

    seat_numbers = [ConvertPasscodeToSeatNumber(passcode) for passcode in input_passcodes]

    print("Max Seat Number: {}".format(max(seat_numbers)))

    missing_seat = FindMissingSeat(seat_numbers)
    print('My seat number is: {}'.format(missing_seat))

