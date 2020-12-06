import math

def calc_lower_upper_bounds(bound, lower, upper, upper_half):
    hold = (lower + upper) / 2
    if bound == upper_half:
        return math.ceil(hold), upper
    return lower, math.floor(hold)

def calc_row(boarding_pass_row, lower, upper):
    for bound in boarding_pass_row:
        lower, upper = calc_lower_upper_bounds(bound, lower, upper, 'B')
    
    if lower < upper:
        return lower
    return upper

def calc_column(boarding_pass_column, lower, upper):
    for bound in boarding_pass_column:
        lower, upper = calc_lower_upper_bounds(bound, lower, upper, 'R')
    
    if lower > upper:
        return lower
    return upper


def calc_boarding_passes(passes, all_passes = []) -> int:
    if not passes:
        return 0, []
    
    prev_seat_id, all_passes = calc_boarding_passes(passes[1:])
    
    boarding_pass = passes[0]
    row = calc_row(boarding_pass[:7], 0, 127)
    column = calc_column(boarding_pass[7:], 0, 7)

    seat_id = (row * 8) + column
    all_passes.append(seat_id)

    return  (seat_id if seat_id > prev_seat_id else prev_seat_id), all_passes


def calc_valid_boarding_passes(passes):
    seat_id, all_passes = calc_boarding_passes(passes)

    all_passes = set(all_passes)
    valid  = set(range(min(all_passes), max(all_passes)))

    return list(valid - all_passes)[0]