from functools import reduce
import re


def calc_sum(instructions: list[tuple[int, int]]) -> int:
    return reduce(lambda acc, x: acc + (x[0] * x[1]), instructions, 0)


def get_real_instructions(input: str) -> list[tuple[int, int]]:
    pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")

    def aux(acc: list[tuple[int, int]], rest: str) -> list[tuple[int, int]]:
        do_idx = rest.find("do()")
        dont_idx = rest.find("don't()", do_idx)

        current_section = rest[do_idx:dont_idx]
        if current_section.strip() == "":
            return acc

        new_acc = acc.copy()
        for match in pattern.finditer(current_section):
            (left, right) = match.groups()
            new_acc.append((int(left), int(right)))

        new_rest = rest[dont_idx:]
        return aux(new_acc, new_rest)

    return aux([], f"do(){input}don't()")


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
