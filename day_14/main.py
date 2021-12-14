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

--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the
submarine. You'll need to run more steps of the pair insertion process;
a total of 40 steps should do it.

In the above example, the most common element is B (occurring
2192039569602 times) and the least common element is H (occurring
3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the
most and least common elements in the result. What do you get if you
take the quantity of the most common element and subtract the quantity
of the least common element?
"""
import os
from collections import defaultdict
from typing import Counter, DefaultDict

InsertionRules = dict[str, str]
PairCounts = DefaultDict[str, int]
CharCounts = DefaultDict[str, int]


def get_pair_counts(string: str) -> PairCounts:
    pair_counts: DefaultDict[str, int] = defaultdict(int)
    for index in range(len(string) - 1):
        pair = string[index : index + 2]
        pair_counts[pair] += 1

    return pair_counts


def iterate(
    pair_counts: PairCounts,
    char_counts: CharCounts,
    rules: InsertionRules,
) -> tuple[PairCounts, CharCounts]:
    new_pair_counts: PairCounts = defaultdict(int)
    for pair, count in pair_counts.items():
        if pair in rules:
            center_char = rules[pair]
            first, second = iter(pair)
            new_pair_1 = first + center_char
            new_pair_2 = center_char + second
            if new_pair_1 in rules:  # TODO: try to remove
                new_pair_counts[new_pair_1] += count
            if new_pair_2 in rules:
                new_pair_counts[new_pair_2] += count

            char_counts[center_char] += count

    return new_pair_counts, char_counts


def iterate_many(
    pair_counts: PairCounts,
    char_counts: CharCounts,
    rules: InsertionRules,
    count: int,
) -> tuple[PairCounts, CharCounts]:
    for _ in range(count):
        pair_counts, char_counts = iterate(pair_counts, char_counts, rules)

    return pair_counts, char_counts


def parse_data(data: str) -> tuple[PairCounts, CharCounts, InsertionRules]:
    template, rule_lines = data.split("\n\n")

    rules = {}
    for line in rule_lines.splitlines():
        pair, char = line.split(" -> ")
        rules[pair] = char

    pair_counts = get_pair_counts(template)
    char_counts: CharCounts = defaultdict(int)
    char_counts.update(Counter(template))
    return pair_counts, char_counts, rules


def part1(data: str) -> int:
    pair_counts, char_counts, rules = parse_data(data)
    pair_counts, char_counts = iterate_many(
        pair_counts,
        char_counts,
        rules,
        count=10,
    )
    return max(char_counts.values()) - min(char_counts.values())


def part2(data: str) -> int:
    pair_counts, char_counts, rules = parse_data(data)
    pair_counts, char_counts = iterate_many(
        pair_counts,
        char_counts,
        rules,
        count=40,
    )
    return max(char_counts.values()) - min(char_counts.values())


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
    pair_counts, char_counts, rules = parse_data(test_data)
    assert pair_counts == {"NN": 1, "NC": 1, "CB": 1}
    assert char_counts == dict(Counter("NNCB"))

    pair_counts, char_counts = iterate(pair_counts, char_counts, rules)
    assert pair_counts == {
        "NC": 1,
        "CN": 1,
        "NB": 1,
        "BC": 1,
        "CH": 1,
        "HB": 1,
    }
    assert char_counts == dict(Counter("NCNBCHB"))

    pair_counts, char_counts = iterate(pair_counts, char_counts, rules)
    assert pair_counts == {
        "NB": 2,
        "BC": 2,
        "CC": 1,
        "CN": 1,
        "BB": 2,
        "CB": 2,
        "BH": 1,
        "HC": 1,
    }
    assert char_counts == dict(Counter("NBCCNBBBCBHCB"))

    assert part1(test_data) == 1588


def test_part2() -> None:
    assert part2(test_data) == 2_188_189_693_529


def main() -> None:
    with open(os.path.join(os.path.dirname(__file__), "input")) as file:
        data = file.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
