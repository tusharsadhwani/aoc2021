import os


def part1(data: str) -> None:
    ...


def part2(data: str) -> None:
    ...


test_data = """\
...
"""


def test_part1() -> None:
    assert part1(test_data) == ...


def test_part2() -> None:
    assert part2(test_data) == ...


def main() -> None:
    with open(os.path.join(os.path.dirname(__file__), "input")) as file:
        data = file.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
