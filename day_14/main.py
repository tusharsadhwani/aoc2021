"""
--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on
your submarine. The submarine has polymerization equipment that would
produce suitable materials to reinforce the submarine, and the nearby
volcanically-active caves should even have the necessary input elements
in sufficient quantities.

The submarine manual contains instructions for finding the optimal
polymer formula; specifically, it offers a polymer template and a list
of pair insertion rules (your puzzle input). You just need to work out
what polymer would result after repeating the pair insertion process a
few times.

For example:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C

The first line is the polymer template - this is the starting point of
the process.

The following section defines the pair insertion rules. A rule like
`AB -> C` means that when elements A and B are immediately adjacent,
element C should be inserted between them. These insertions all happen
simultaneously.

So, starting with the polymer template NNCB, the first step
simultaneously considers all three pairs:

- The first pair (NN) matches the rule NN -> C, so element C is inserted
  between the first N and the second N.
- The second pair (NC) matches the rule NC -> B, so element B is
  inserted between the N and the C.
- The third pair (CB) matches the rule CB -> H, so element H is inserted
  between the C and the B.

Note that these pairs overlap: the second element of one pair is the
first element of the next pair. Also, because all pairs are considered
simultaneously, inserted elements are not considered to be part of a
pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

This polymer grows quickly. After step 5, it has length 97; After step
10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298
times, H occurs 161 times, and N occurs 865 times; taking the quantity
of the most common element (B, 1749) and subtracting the quantity of the
least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the
most and least common elements in the result. What do you get if you
take the quantity of the most common element and subtract the quantity
of the least common element?
"""
import os
from typing import Counter, Generator

InsertionRules = dict[str, str]


def get_pair_chars(string: str) -> Generator[str, None, None]:
    for index in range(len(string) - 1):
        yield string[index : index + 2]


def iterate(template: str, rules: InsertionRules) -> str:
    insertions: list[tuple[int, str]] = []
    for index, pair in enumerate(get_pair_chars(template), start=1):
        if pair in rules:
            insertions.append((index, rules[pair]))

    chars = list(template)
    insertions.sort(reverse=True)
    for index, char in insertions:
        chars.insert(index, char)

    return "".join(chars)


def iterate_many(template: str, rules: InsertionRules, count: int) -> str:
    for _ in range(count):
        template = iterate(template, rules)

    return template


def parse_data(data: str) -> tuple[str, InsertionRules]:
    template, rule_lines = data.split("\n\n")

    rules = {}
    for line in rule_lines.splitlines():
        pair, char = line.split(" -> ")
        rules[pair] = char

    return template, rules


def part1(data: str) -> str:
    template, rules = parse_data(data)
    string = iterate_many(template, rules, count=10)

    (_, max_char_count), *_, (_, min_char_count) = Counter(string).most_common()
    return max_char_count - min_char_count


def part2(data: str) -> None:
    ...


test_data = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def test_part1() -> None:
    template, rules = parse_data(test_data)
    assert iterate_many(template, rules, count=1) == "NCNBCHB"
    assert iterate_many(template, rules, count=2) == "NBCCNBBBCBHCB"
    assert iterate_many(template, rules, count=3) == "NBBBCNCCNBBNBNBBCHBHHBCHB"
    assert (
        iterate_many(template, rules, count=4)
        == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    )

    assert part1(test_data) == 1588


def test_part2() -> None:
    assert part2(test_data) == ...


def main() -> None:
    with open(os.path.join(os.path.dirname(__file__), "input")) as file:
        data = file.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
