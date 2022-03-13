from functools import total_ordering


@total_ordering
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other) -> bool:
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        if p1 > p2: 
            p1, p2 = p2, p1
        self.start = p1
        self.end = p2

        self.vertical = (p1.x == p2.x)
        self.horizontal = (p1.y == p2.y)
        self.diagonal = (abs(p1.x - p2.x) == abs(p1.y - p2.y))

    def generate_all_points(self, include_diagonal: bool=False) -> Point:
        p1, p2 = self.start, self.end

        if self.vertical or self.horizontal:
            for a in range(p1.x, p2.x + 1):
                for b in range(p1.y, p2.y + 1):
                    yield Point(a, b)
        elif self.diagonal and include_diagonal:
            for a in range(p1.x, p2.x + 1):
                if p2.y > p1.y:
                    b = p1.y + (a - p1.x)
                else:
                    b = p1.y - (a - p1.x)
                yield Point(a, b)  


def load_data(path: str) -> str:
    with open(path, mode='r', encoding="utf-8") as f:
        return f.read()


def parse_data(data: str) -> Line:
    for i in data.split('\n'):
        p1, p2 = i.replace(' ', '').split('->')        
        p1 = Point(*map(int, p1.split(',')))
        p2 = Point(*map(int, p2.split(',')))
        yield Line(p1, p2)


def puzzle_one(data: str, include_diagonal: bool=False) -> int:
    overlapping_points = {}
    for line in parse_data(data):
        for point in line.generate_all_points(include_diagonal=include_diagonal):
            overlapping_points[point] = overlapping_points.get(point, 0) + 1 
    return sum(1 for (k, v) in overlapping_points.items() if v > 1)


def puzzle_two(data: str) -> int:
    return puzzle_one(data, include_diagonal=True)


if __name__ == "__main__":    
    print('--------------', 'Puzzle One', '--------------', end='\n')
    print(puzzle_one(load_data("../puzzle_input.txt")))
    print('--------------', 'Puzzle Two', '--------------', end='\n')
    print(puzzle_two(load_data("../puzzle_input.txt")))
