DIGIT_SEGMENTS = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}


def load_data(path: str) -> list:
    with open(path, mode="r", encoding="utf-8") as f:
        return [line.replace(" | ", "|").split("|") for line in f.read().splitlines()]


def puzzle_one(data: list) -> int:
    return sum(
        sum(1 for o in outputs.split(" ") if len(DIGIT_SEGMENTS[len(o)]) == 1)
        for outputs in [i[1] for i in data]
    )


def puzzle_two(data: str) -> int:
    result = 0

    for patterns, outputs in data:
        no_top_bottom = {len(p): set(p) for p in patterns.split() if len(p) in (2, 4)}
        four_digits = ""

        for output in outputs.split():
            segments = len(output)
            if segments in (2, 3, 4, 7):
                four_digits += str(DIGIT_SEGMENTS[segments][0])
                continue

            set_output = set(output)
            if segments == 5:
                if len(set_output & no_top_bottom[2]) == 2:
                    four_digits += "3"
                elif len(set_output & no_top_bottom[4]) == 2:
                    four_digits += "2"
                else:
                    four_digits += "5"
            else:  # 6
                if len(set_output & no_top_bottom[2]) == 1:
                    four_digits += "6"
                elif len(set_output & no_top_bottom[4]) == 4:
                    four_digits += "9"
                else:
                    four_digits += "0"

        result += int(four_digits)

    return result


if __name__ == "__main__":
    print("--------------", "Puzzle One", "--------------", end="\n")
    print(puzzle_one(load_data("../puzzle_input.txt")))
    print("--------------", "Puzzle Two", "--------------", end="\n")
    print(puzzle_two(load_data("../puzzle_input.txt")))
