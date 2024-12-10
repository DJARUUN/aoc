from functools import reduce
import re


def calc_sum(instructions: list[tuple[int, int]]) -> int:
    return reduce(lambda acc, x: acc + (x[0] * x[1]), instructions, 0)


def get_real_instructions(input: str) -> list[tuple[int, int]]:
    pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")

    instructions: list[tuple[int, int]] = []
    for match in pattern.finditer(input):
        (left, right) = match.groups()
        instructions.append((int(left), int(right)))

    return instructions


def get_input(filename: str) -> str:
    with open(filename) as f:
        contents = f.read()
        return contents


def main():
    input = get_input("input")
    instructions = get_real_instructions(input)
    result = calc_sum(instructions)
    print(result)


if __name__ == "__main__":
    main()
