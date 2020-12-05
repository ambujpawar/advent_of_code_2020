
MANDATORY_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
OPTIONAL_KEYS = ['cid']
EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
HAIR_COLOR = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


def ReadInput(file_path):
    input_file = open(file_path, "r")
    input_strings = input_file.readlines()
    lines_list = [line.strip() for line in input_strings]
    return lines_list


def SeperateIndividualPassport(list_input_string):
    """
    Separate input from lists of lists to a list per passport
    """
    passports_list = []
    passport_details = ''

    for input_line in list_input_string:
        if input_line == '':
            passports_list.append(passport_details)
            passport_details = ''
        else:
            passport_details = passport_details + input_line + ' '

    return passports_list


def MakeDictFromListOfStrings(list_strings):
    passport = {}
    list_passports = []
    for str_passport in list_strings:
        passport_words = str_passport.split()

        for word in passport_words:
            index_colon = word.find(':')
            passport[word[:index_colon]] = word[index_colon + 1:].rstrip()

        list_passports.append(passport)
        passport = {}

    return list_passports


def NumInvalidPassports(passports):
    invalid_passports = 0
    for passport in passports:
        for key in MANDATORY_KEYS:
            if key not in passport.keys():
                invalid_passports += 1
                break

    return invalid_passports


def ShouldGoFurther(passport):
    is_valid = True
    for key in MANDATORY_KEYS:
        if key not in passport.keys():
            is_valid = False
    return is_valid


def PassportsValidForPart2(passports):
    valid_passports = 0
    for passport in passports:

        if not ShouldGoFurther(passport):
            continue

        if not (len(passport['byr']) == 4 and 1920<=int(passport['byr'])<=2020):
            continue

        if not (len(passport['iyr']) == 4 and 2010<=int(passport['iyr'])<=2020):
            continue

        if not (len(passport['eyr']) == 4 and 2020<=int(passport['eyr'])<=2030):
            continue

        # Height Filter
        if 'cm' in passport['hgt']:
            height = int(passport['hgt'][:passport['hgt'].find('cm')])
            if not 150 <= height <= 193:
                continue
        elif 'in' in passport['hgt']:
            height = int(passport['hgt'][:passport['hgt'].find('in')])
            if not 59 <= height <= 76:
                continue
        else:
            continue

        # Hair color filter
        if not len(passport['hcl'])==7:
            continue

        if passport['hcl'][0] == '#':
            hcl_valid_character = [True for letter in passport['hcl'][1:] if letter in HAIR_COLOR]
            if not len(hcl_valid_character) == 6:
                continue
        else:
            continue
        # Eye color filter
        if passport['ecl'] not in EYE_COLORS:
            continue

        # Passport id filter
        if not len(passport['pid']) == 9:
            continue

        valid_passports += 1

    return valid_passports


if __name__ == '__main__':

    # Read the input
    input_as_strings_list = ReadInput('/Users/ambuj/Desktop/advent_of_code/data/day_4.txt')
    input_as_strings_list = SeperateIndividualPassport(input_as_strings_list)
    passport_candidates = MakeDictFromListOfStrings(input_as_strings_list)

    invalid_passports = NumInvalidPassports(passport_candidates)
    print('Number of valid passports for part 1: {}'.format(len(passport_candidates) - invalid_passports))

    valid_passports_part_2 = PassportsValidForPart2(passport_candidates)
    print('Number of valid passports for part 2: {}'.format(valid_passports_part_2))

    print('DONE!')