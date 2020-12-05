from year_2020.day_4 import part_1, part_2


def test_part_1_sample(day_4_sample):
    results = part_1(day_4_sample)
    assert results == 2


def test_part_1(day_4_input):
    results = part_1(day_4_input)
    assert results == 264


def test_part_2_sample(day_4_sample):
    results = part_2(day_4_sample)
    assert results == 2


def test_part_2(day_4_input):
    results = part_2(day_4_input)
    assert results == 224