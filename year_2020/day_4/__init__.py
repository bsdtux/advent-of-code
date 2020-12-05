import re

def create_passports_from_parts(passport):
    part_list = list()
    temp_dict = {}

    for part in passport:
        if part == '':
            part_list.append(temp_dict)
            temp_dict = {}
            continue
        psplit = part.split(' ')
        temp_dict.update(dict([d.split(':') for d in psplit]))

    part_list.append(temp_dict)
    return part_list


def validate_passport(passport):
    req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return not req - set(passport.keys())


def passport_scanner(passport_list):
    # Create Passport from parts
    passports = create_passports_from_parts(passport_list)
   
    # Validate passport list individual items
    valid = [val for val in passports if validate_passport(val)]
    return valid


def pattern_matched(needs_validated):
    patterns = {
        'byr':'19[2-9][0-9]|200[0-2]',
        'iyr':'20(1[0-9]|20)',
        'eyr':'202[0-9]|2030',
        'hgt':'1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in',
        'hcl':'#[0-9a-f]{6}',
        'ecl':'amb|blu|brn|gry|grn|hzl|oth',
        'pid':'[0-9]{9}',
    }

    for key, val in needs_validated.items():
        if patterns.get(key) and not re.fullmatch(patterns[key], val):
            return False
    return True


def part_1(passport_list):
    return len(passport_scanner(passport_list))

def part_2(passport_list):
    valid = passport_scanner(passport_list)
    return len(list(filter(pattern_matched, valid)))