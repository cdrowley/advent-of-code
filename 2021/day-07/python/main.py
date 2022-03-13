def load_data(path: str) -> list:
    with open(path, mode='r', encoding="utf-8") as f:
        return list(map(int, f.read().split(',')))


def puzzle_one(data: list) -> int:
    min_fuel_cost = float('inf')
    for i in range(min(data), max(data)):
        min_fuel_cost = min(min_fuel_cost, sum(abs(h - i) for h in data))
    return min_fuel_cost


def puzzle_two(data: str) -> int:
    fuel_use = lambda n: sum(i for i in range(1, n + 1))
    
    min_fuel_cost = float('inf')
    for i in range(min(data), max(data)):
        min_fuel_cost = min(min_fuel_cost, sum(fuel_use(abs(i - j)) for j in data))
    return min_fuel_cost

if __name__ == "__main__":    
    print('--------------', 'Puzzle One', '--------------', end='\n')
    print(puzzle_one(load_data("../puzzle_input.txt")))
    print('--------------', 'Puzzle Two', '--------------', end='\n')
    print(puzzle_two(load_data("../puzzle_input.txt")))
