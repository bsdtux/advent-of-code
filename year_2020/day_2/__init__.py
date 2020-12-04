import typing as ty
from collections import Counter

def meets_password_policy_count(
    min_requirement, max_requirement, character, password):
    count = Counter(password)
    if count.get(character) and (
        min_requirement <= count[character] <= max_requirement):
        return True
    return False

def meets_password_policy_positional(
    min_requirement, max_requirement, character, password):

    if (password[min_requirement-1] == character and 
        password[max_requirement-1] != character):
        return True
    
    if (password[min_requirement-1] != character and 
        password[max_requirement-1] == character):
        return True
    
    return False

def get_requirements_password_from_str(req_str: str) -> ty.Tuple:
    requirements, password = list(map(
        lambda x: x.strip(), req_str.split(':')))
    num_req, ch_req = requirements.split(' ')
    min_req, max_req = num_req.split('-')

    return (int(min_req), int(max_req), ch_req, password)


def num_of_valid_passwords(passwords: list, pol_type: str = 'count') -> int:
    valid_count = 0
    pass_map = {
        'count': meets_password_policy_count,
        'pos': meets_password_policy_positional
    }

    func = pass_map.get(pol_type) or pass_map['count']

    user_pass = [get_requirements_password_from_str(
        user_reqs) for user_reqs in passwords]
    valid_count = len(list(filter(lambda x: func(*x), user_pass)))
    
    return valid_count
