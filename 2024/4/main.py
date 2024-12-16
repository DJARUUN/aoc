def get_input(filename: str) -> str:
    with open(filename) as f:
        contents = f.read()
        return contents


def create_matrix(input: str) -> list[list[str]]:
    lines = input.splitlines()
    matrix = list(map(lambda line: list(line), lines))
    return matrix


def check_pos(matrix: list[list[str]], supposed_to_be: str, x: int, y: int) -> bool:
    if x < 0 or y < 0 or x > len(matrix[0]) - 1 or y > len(matrix) - 1:
        return False

    letter = matrix[y][x]

    return letter == supposed_to_be


WORD = "XMAS"


def word_search(matrix: list[list[str]]) -> int:
    correct_count = 0

    for y in range(len(matrix)):
        row = matrix[y]

        for x in range(len(row)):
            letter = matrix[y][x]
            if letter != WORD[0]:
                continue

            is_corrects = [
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
            ]

            for offset in range(1, len(WORD)):
                positions = [
                    (x + offset, y),
                    (x - offset, y),
                    (x, y + offset),
                    (x, y - offset),
                    (x + offset, y + offset),
                    (x + offset, y - offset),
                    (x - offset, y + offset),
                    (x - offset, y - offset),
                ]

                supposed_to_be = WORD[offset]

                for i, (x_pos, y_pos) in enumerate(positions):
                    is_corrects[i] = is_corrects[i] and check_pos(
                        matrix, supposed_to_be, x_pos, y_pos
                    )

            for j, is_correct in enumerate(is_corrects):
                if is_correct:
                    correct_count += 1
                    print(f"CORRECT: {x} {y} {j}")

    return correct_count


def main():
    input = get_input("input")
    matrix = create_matrix(input)
    result = word_search(matrix)
    print(result)


if __name__ == "__main__":
    main()
