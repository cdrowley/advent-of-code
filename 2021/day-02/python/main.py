def load_parse_data(path: str) -> list:
    """
    Reads puzzle input and returns a list of tuples with direction (string) and magnitude (int).
    Input:      'Forward 10\nDown 6'
    Output:     [('Forward', 10), ('Down', 6)]
    """
    with open(path, mode='r', encoding="utf-8") as f:
        return [(i.split(' ')[0], int(i.split(' ')[1])) for i in f.read().split('\n')]


def puzzle_one(steps: list) -> int:
    position, depth = 0, 0

    for step in steps:
        if step[0] == 'forward':
            position += step[1]
        elif step[0] == 'down':
            depth += step[1]
        else:
            depth -= step[1]
  
    return position * depth
    

def puzzle_two(steps: list) -> int:
    position, depth, aim = 0, 0, 0

    for step in steps:
        if step[0] == 'forward':
            position += step[1]
            depth += aim * step[1]
        elif step[0] == 'down':
            aim += step[1]
        else:
            aim -= step[1]

    return position * depth

if __name__ == "__main__":
    print('--------------', 'Puzzle One', '--------------', end='\n')
    print(puzzle_one(load_parse_data('../puzzle_input.txt')))

    print('--------------', 'Puzzle Two', '--------------', end='\n')
    print(puzzle_two(load_parse_data('../puzzle_input.txt')))
