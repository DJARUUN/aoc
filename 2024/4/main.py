def get_input(filename: str) -> str:
    with open(filename) as f:
        contents = f.read()
        return contents


def create_matrix(input: str) -> list[list[str]]:
    lines = input.splitlines()
    matrix = list(map(lambda line: list(line), lines))
    return matrix


def get_letter_at_pos(matrix: list[list[str]], x: int, y: int) -> str | None:
    if x < 0 or y < 0 or x > len(matrix[0]) - 1 or y > len(matrix) - 1:
        return None

    letter = matrix[y][x]
    return letter


WORD = "MAS"


def word_search(matrix: list[list[str]]) -> int:
    correct_count = 0

    for y, row in enumerate(matrix):
        for x, letter in enumerate(row):
            if letter != WORD[1]:
                continue

            positions = [(x + 1, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1)]

            letters: list[str] = []

            is_valid = True
            for x_pos, y_pos in positions:
                letter = get_letter_at_pos(matrix, x_pos, y_pos)
                if not letter:
                    is_valid = False
                    continue

                letters.append(letter)

            if not is_valid:
                continue

            diagonal_1 = letters[0] + letters[1]
            diagonal_2 = letters[2] + letters[3]

            if (diagonal_1 == "MS" or diagonal_1 == "SM") and (
                diagonal_2 == "MS" or diagonal_2 == "SM"
            ):
                correct_count += 1

    return correct_count


def main():
    input = get_input("input")
    matrix = create_matrix(input)
    result = word_search(matrix)
    print(result)


if __name__ == "__main__":
    main()
