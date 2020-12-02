import typing as ty


def find_2020_sum_from_expense_list(expense_list: ty.List) -> ty.Tuple:
    for i in range(len(expense_list)):
        for j in range(len(expense_list)):
            if expense_list[i] + expense_list[j] == 2020:
                return expense_list[i], expense_list[j]
    return None, None


def find_2020_sum_from_expense_list_2(expense_list: ty.List) -> ty.Tuple:
    for i in range(len(expense_list)):
        for j in range(len(expense_list)):
            for k in range(len(expense_list)):
                if expense_list[i] + expense_list[j] + expense_list[k] == 2020:
                    return [expense_list[i], expense_list[j], expense_list[k]]
    return []

# Todo: reduce these to recursive functions
