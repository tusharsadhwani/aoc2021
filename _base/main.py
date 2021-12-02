import os


def part1() -> None:
    ...


def part2() -> None:
    ...


test_data = """\
...
"""


def test_part1() -> None:
    ...


def test_part2() -> None:
    ...


def main() -> None:
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        data = file.read()

    part1()
    part2()


if __name__ == "__main__":
    main()
