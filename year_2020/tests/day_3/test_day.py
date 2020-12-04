from year_2020.day_3 import get_encountered_trees, move_by_patterns

mock_sample = [
'..##.........##.........##.........##.........##.........##.......',
'#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..',
'.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.',
'..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#',
'.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.',
'..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....',
'.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#',
'.#........#.#........#.#........#.#........#.#........#.#........#',
'#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...',
'#...##....##...##....##...##....##...##....##...##....##...##....#',
'.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#',
]

def test_get_encountered_trees_sample():
    results = get_encountered_trees(mock_sample, 3, 1)
    assert results == 7

def test_get_encountered_trees(day_3_input):
    results = get_encountered_trees(day_3_input, 3, 1)
    assert results == 272

def test_move_by_patterns_sample():
    move_patterns = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = move_by_patterns(mock_sample, move_patterns)
    assert results == 336

def test_move_by_patterns_(day_3_input):
    move_patterns = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = move_by_patterns(day_3_input, move_patterns)
    assert results == 3898725600