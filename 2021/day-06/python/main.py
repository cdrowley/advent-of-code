def load_parse_data(path: str) -> list:
    with open(path, mode='r', encoding="utf-8") as f:
        return list(map(int, f.read().split(',')))


def school_by_age(data: list) -> list:
    school_by_age = [0] * 9
    for age in data:
        school_by_age[age] += 1
    return school_by_age


def model_school_growth(school_by_age: list, days: int=80) -> list:
    for _ in range(days):
        reproduction_rate = school_by_age[0]
        for age in range(8):
            school_by_age[age] = school_by_age[age + 1]
        school_by_age[6] += reproduction_rate
        school_by_age[8] = reproduction_rate
    return school_by_age


def puzzle_one(data: list) -> int:
    return sum(model_school_growth(school_by_age(data)))


def puzzle_two(data: str) -> int:
    return sum(model_school_growth(school_by_age(data), days=256))


if __name__ == "__main__":    
    print('--------------', 'Puzzle One', '--------------', end='\n')
    print(puzzle_one(load_parse_data("../puzzle_input.txt")))
    print('--------------', 'Puzzle Two', '--------------', end='\n')
    print(puzzle_two(load_parse_data("../puzzle_input.txt")))
