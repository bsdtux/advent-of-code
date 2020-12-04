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
