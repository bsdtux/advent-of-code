from year_2020.day_5 import calc_boarding_passes, calc_valid_boarding_passes

def test_calc_boarding_passes_part_1_sample(day_5_sample):
    assert calc_boarding_passes(day_5_sample)[0] == 820

def test_calc_boarding_passes_part_1(day_5_input):
    assert calc_boarding_passes(day_5_input)[0] == 915

def test_calc_boarding_passes_part_2_sample(day_5_sample):
    assert calc_valid_boarding_passes(day_5_sample) == 120

def test_calc_boarding_passes_part_2(day_5_input):
    assert calc_valid_boarding_passes(day_5_input) == 699