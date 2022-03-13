from collections import Counter


def load_data(path: str) -> list:
    """
    Reads puzzle input and returns a list of binary strings.
    Input:      '00100\n11110'
    Output:     ['00100', '11110']
    """
    with open(path, mode='r', encoding="utf-8") as f:
        return [i for i in f.read().split('\n')]


def get_column(matrix: list, col_num: int) -> list: 
    return [c[col_num] for c in matrix]


def most_common_bit(li: list) -> str:
    most_common = Counter(li).most_common()
    if len(most_common) != 1 and most_common[0][1] == most_common[1][1]:
        return '1'    
    return most_common[0][0]


def least_common_bit(li: list) -> str:
    least_common = Counter(li).most_common()
    if len(least_common) != 1 and least_common[0][1] == least_common[1][1]:
        return '0'    
    return least_common[-1][0]


def flip_bits(binary_string: str) -> str:
    return ''.join('1' if b == '0' else '0' for b in binary_string)


def binary_to_decimal(b: str) -> int:
    return 0 if b == "" else int(b[-1]) + 2 * binary_to_decimal(b[:-1])


def puzzle_one(data: list) -> int:
    gamma = "".join([most_common_bit(get_column(data, col_idx)) for col_idx in range(len(data[0]))])
    epsilon = binary_to_decimal(flip_bits(gamma))
    gamma = binary_to_decimal(gamma)
    
    return gamma * epsilon

    
def puzzle_two(data: list) -> int:
    oxygen_candidates = data.copy()
    carbon_candidates = data.copy()

    for col_idx in range(len(data[0])):
        if len(oxygen_candidates) > 1:
            most_common = most_common_bit(get_column(oxygen_candidates, col_idx))
            oxygen_candidates = [i for i in oxygen_candidates if i[col_idx] == most_common]
        
        if len(carbon_candidates) > 1:
            least_common = least_common_bit(get_column(carbon_candidates, col_idx))
            carbon_candidates = [i for i in carbon_candidates if i[col_idx] == least_common]
        
    oxygen_generator_rating = binary_to_decimal(oxygen_candidates[0])
    carbon_scrubber_rating = binary_to_decimal(carbon_candidates[0])
    
    return oxygen_generator_rating * carbon_scrubber_rating
    

if __name__ == "__main__":
    print('--------------', 'Puzzle One', '--------------', end='\n')
    print(puzzle_one(load_data('../puzzle_input.txt')))
    print('--------------', 'Puzzle Two', '--------------', end='\n')
    print(puzzle_two(load_data('../puzzle_input.txt')))
