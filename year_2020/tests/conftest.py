import pytest


def open_file(day: str) -> str:
    data = []
    with open(f'year_2020/tests/fixtures/day_{day}.txt') as infile:
        lines = infile.read().splitlines()
        data = lines
    
    return data


@pytest.fixture
def day_2_input():
    return open_file('2')

@pytest.fixture
def day_3_input():
    return open_file('3')

@pytest.fixture
def day_4_sample():
    return open_file('4_sample')

@pytest.fixture
def day_4_input():
    return open_file('4')

@pytest.fixture
def day_5_sample():
    return open_file('5_sample')

@pytest.fixture
def day_5_input():
    return open_file('5')