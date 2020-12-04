import typing as ty
from itertools import combinations
from functools import reduce


def find_combinations_2020(expense_list, k):
    result = list(filter(
        lambda x: sum(x) == 2020, list(combinations(expense_list, k))))
    return reduce(lambda x, y: x * y, result[0])
