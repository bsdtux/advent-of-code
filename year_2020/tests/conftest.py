import pytest


def open_file(day: str) -> str:
    data = []
    with open(f'year_2020/tests/fixtures/day_{day}.txt') as infile:
        lines = infile.readlines()
        data = lines
    
    return data


@pytest.fixture
def day_2_input():
    return open_file('2')