def puzzle_one_approach_one(input_data: str) -> int:
    depths = [int(d) for d in input_data.split('\n')]
    changes = ['(increased)' if (depths[idx] - depth) < 0 else '(decreased or same)' for idx, depth in enumerate(depths[1:])]  
    return changes.count('(increased)')


def puzzle_one_approach_two(input_data: str) -> int:
    cnt = 0
    for idx, depth in enumerate(map(int, input_data.split())):
        if idx == 0:
            last_depth = depth
            continue
        cnt += 1 if (last_depth - depth) < 0 else 0
        last_depth = depth
    return cnt


def puzzle_one_approach_three(input_data: str) -> int:
    depths = list(map(int, input_data.split('\n')))
    return sum(1 if d2 > d1 else 0 for d1, d2 in zip(depths, depths[1:]))


def puzzle_one_approach_four(input_data: str) -> int:
    import numpy as np
    depths = np.fromstring(input_data, dtype=int, sep='\n')
    return int(np.sum(np.diff(depths, n=1) > 0))


def puzzle_two_approach_one(input_data: str) -> int:
    depths = [int(d) for d in input_data.split('\n')]
    sliding_window = [sum(depths[idx:idx+3]) for idx, depth in enumerate(depths[2:])]
    changes = ['(increased)' if (sliding_window[idx] - sw) < 0 else '(decreased or same)' for idx, sw in enumerate(sliding_window[1:])]  
    return changes.count('(increased)')


def puzzle_two_approach_two(input_data: str) -> int:
    cnt = 0
    for idx, depth in enumerate(map(int, input_data.split())):
        if idx == 0:
            d1 = depth
            continue
        elif idx == 1:
            d2 = depth
            continue

        sliding_window = d1 + d2 + depth

        if idx == 2:
            d1, d2 = d2, depth
            last_sliding_window = sliding_window
            continue
        
        cnt += 1 if (last_sliding_window - sliding_window) < 0 else 0
        d1, d2 = d2, depth
        last_sliding_window = sliding_window    
    return cnt


def puzzle_two_approach_three(input_data: str) -> int:
    import pandas as pd
    sliding_window = (
        pd.DataFrame(list(map(int, input_data.split('\n'))))
        .rolling(3)
        .sum()
        )
    
    increases = (
        sliding_window
        .diff() > 0
        ).sum()

    return int(increases)


if __name__ == "__main__":
    with open("../puzzle_input.txt", mode='r', encoding="utf-8") as f:
        input_data = f.read()

    print('--------------', 'Puzzle One', '--------------', end='\n')
    print(puzzle_one_approach_one(input_data))
    print(puzzle_one_approach_two(input_data))
    print(puzzle_one_approach_three(input_data))
    print(puzzle_one_approach_four(input_data))

    print('--------------', 'Puzzle Two', '--------------', end='\n')
    print(puzzle_two_approach_one(input_data))
    print(puzzle_two_approach_two(input_data))
    print(puzzle_two_approach_three(input_data))
