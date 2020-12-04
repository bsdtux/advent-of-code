from year_2020.day_2 import num_of_valid_passwords


mock_sample = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc'
]

def test_num_of_valid_passwords_sample():
    results = num_of_valid_passwords(mock_sample)
    assert results == 2


def test_num_of_valid_passwords(day_2_input):
    results = num_of_valid_passwords(day_2_input)
    assert results == 434


def test_num_of_valid_passwords_sample():
    results = num_of_valid_passwords(mock_sample, 'pos')
    assert results == 1


def test_num_of_valid_passwords(day_2_input):
    results = num_of_valid_passwords(day_2_input, 'pos')
    assert results == 509