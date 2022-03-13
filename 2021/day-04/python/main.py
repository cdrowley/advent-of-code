class BingoBoard:
    def __init__(self, board: list) -> None:
        self.board_numbers = dict.fromkeys([item for sublist in board for item in sublist], "Not Marked")
        self.lines = board + self.get_columns(board)
        self.bingo = False
        self.winning_line = None
        self.last_number = None

    def __str__(self) -> str:
        return f"{self.board_numbers}"

    def get_columns(self, board) -> list:
        return [tuple(row[cidx] for row in board) for cidx in range(len(board[0]))]

    def mark(self, number: int) -> None:
        if not self.winning_line:
            self.last_number = number
            self.board_numbers[number] = "Marked"
            
    def is_marked(self, number: int) -> bool:
        return self.board_numbers[number] == "Marked"

    def line_is_bingo(self, line: list) -> bool:
        win = all(map(self.is_marked, line))
        if win:
            self.winning_line = line
            self.bingo = True
            return True
        return False
        
    def is_bingo(self) -> bool:
        if self.bingo:
            return True
        return any(map(self.line_is_bingo, self.lines))

    def get_unmarked_numbers(self) -> list:
        return [k for (k, v) in self.board_numbers.items() if v == "Not Marked"]
    
    def final_score(self) -> int:
        return sum(self.get_unmarked_numbers()) * self.last_number


def load_parse_data(path: str) -> list:
    """Reads puzzle input and returns a list of bingo numbers to be called and a list of BingoBoards."""
    with open(path, mode='r', encoding="utf-8") as f:
        data = f.read().replace('\n\n', '\n').split('\n')
        numbers = list(map(int, data[0].split(',')))
        boards = [tuple(map(int, i.replace('  ', ' ').strip().split(' '))) for i in data[1:]]
        boards = [BingoBoard(boards[i:i+5]) for i in range(0, len(boards), 5)]
        return [numbers, boards]


def puzzle_one(data: list) -> int:
    def mark_and_check(bingo_boards: list, number: int) -> BingoBoard:
        for bb in bingo_boards:
            bb.mark(number)
            if bb.is_bingo():
                return bb

    numbers, bingo_boards = data

    for number in numbers:
        winning_bingo_board = mark_and_check(bingo_boards, number)
        if winning_bingo_board:
            break

    return winning_bingo_board.final_score()


def puzzle_two(data: list) -> int:
    numbers, bingo_boards = data
    winning_boards = []

    for number in numbers:
        current_boards = [bb for bb in bingo_boards if bb.bingo == False]
        for cb in current_boards:
            cb.mark(number)
            if cb.is_bingo():
                winning_boards.append(cb) 

    return winning_boards[-1].final_score()


if __name__ == "__main__":    
    print('--------------', 'Puzzle One', '--------------', end='\n')
    print(puzzle_one(load_parse_data('../puzzle_input.txt')))
    print('--------------', 'Puzzle Two', '--------------', end='\n')
    print(puzzle_two(load_parse_data('../puzzle_input.txt')))
