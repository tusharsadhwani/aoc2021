"""
--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the
cave mouth, collapsing it. Sensors indicate another exit to this cave at
a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you
notice that the four-digit seven-segment displays in your submarine are
malfunctioning; they must have been damaged during the escape. You'll be
in a lot of trouble without them, so you'd better figure out what's
wrong.

Each digit of a seven-segment display is rendered by turning on or off
any of seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

So, to render a 1, only segments c and f would be turned on; the rest
would be off. To render a 7, only segments a, c, and f would be turned
on.

The problem is that the signals which control the segments have been
mixed up on each display. The submarine is still trying to display
numbers by producing output on signal wires a through g, but those wires
are connected to segments randomly. Worse, the wire/segment connections
are mixed up separately for each four-digit display! (All of the digits
within a display use the same connections, though.)

So, you might know that only signal wires b and g are turned on, but
that doesn't mean segments b and g are turned on: the only digit that
uses two segments is 1, so it must mean segments c and f are meant to be
on. With just that information, you still can't tell which wire (b/g)
goes to which segment (c/f). For that, you'll need to collect more
information.

For each display, you watch the changing signals for a while, make a
note of all ten unique signal patterns you see, and then write down a
single four digit output value (your puzzle input). Using the signal
patterns, you should be able to work out which pattern corresponds to
which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf

(The entry is wrapped here to two lines so it fits; in your notes, it
will all be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and
finally the four digit output value. Within an entry, the same
wire/segment connections are used (but you don't know what the
connections actually are). The unique signal patterns correspond to the
ten different ways the submarine tries to render a digit using the
current wire/segment connections. Because 7 is the only digit that uses
three segments, dab in the above example means that to render a 7,
signal lines d, a, and b are on. Because 4 is the only digit that uses
four segments, eafb means that to render a 4, signal lines e, a, f, and
b are on.

Using this information, you should be able to work out which combination
of signal wires corresponds to each of the ten digits. Then, you can
decode the four digit output value. Unfortunately, in the above example,
all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five
segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce

Because the digits 1, 4, 7, and 8 each use a unique number of segments,
you should be able to tell which combinations of signals correspond to
those digits. Counting only digits in the output values (the part after
| on each line), in the above example, there are 26 instances of digits
that use a unique number of segments.

In the output values, how many times do digits 1, 4, 7, or 8 appear?

--- Part Two ---
Through a little deduction, you should now be able to determine the
remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf

After some careful analysis, the mapping between signal wires and
segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc

So, the unique signal patterns would correspond to the following digits:

- acedgfb: 8
- cdfbe: 5
- gcdfa: 2
- fbcad: 3
- dab: 7
- cefabd: 9
- cdfgeb: 6
- eafb: 4
- cagedb: 0
- ab: 1

Then, the four digits of the output value can be decoded:

- cdfeb: 5
- fcadb: 3
- cdfeb: 5
- cdbaf: 3

Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example
above, the output value of each entry can be determined:

- fdgacbe cefdb cefbgd gcbe: 8394
- fcgedb cgb dgebacf gc: 9781
- cg cg fdcagb cbg: 1197
- efabcd cedba gadfec cb: 9361
- gecf egdcabf bgf bfgea: 4873
- gebdcfa ecba ca fadegcb: 8418
- cefg dcbef fcge gbcadfe: 4548
- ed bcgafe cdgba cbgef: 1625
- gbdfcae bgc cg cgb: 8717
- fgae cfgab fg bagce: 4315

Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode
the four-digit output values. What do you get if you add up all of the
output values?
"""
import os
from itertools import permutations
from typing import Sequence

Digit = frozenset[str]


def parse_input(data: str) -> tuple[list[list[Digit]], list[list[Digit]]]:
    all_digits: list[list[Digit]] = []
    input_digits: list[list[Digit]] = []
    for line in data.splitlines():
        digits_text, input_text = line.split("|")
        all_digits.append([frozenset(segments) for segments in digits_text.split()])
        input_digits.append([frozenset(segments) for segments in input_text.split()])

    return all_digits, input_digits


def part1(data: str) -> int:
    _, input_digits = parse_input(data)

    count_1478 = 0
    for row in input_digits:
        for digits in row:
            if len(digits) not in (5, 6):
                count_1478 += 1

    return count_1478


def get_set_from_word(permutation: Sequence[int], digit: Digit) -> set[int]:
    """
    Returns a digit set from a given digit word,
    based on the current permutation.

    i.e. if:
    permutation = [6, 5, 4, 3, 2, 1, 0]
    digit = 'abcd'

    then output = {6, 5, 4, 3}
    """
    return {permutation[ord(char) - ord("a")] for char in digit}


def part2(data: str) -> int:
    """
    Assuming the seven segment display in this order:

         0000
        1    2
        1    2
         3333
        4    5
        4    5
         6666

    The digits are defined by the activated segments.

    The idea is to generate all possible permutations of a to g
    mappings between these 1-7 values, and then vlalidate the words
    against them until we find one in which none of the given words
    generate an invalid number.
    """
    digit_sets = (
        {0, 1, 2, 4, 5, 6},  # Zero
        {2, 5},  # One
        {0, 2, 3, 4, 6},  # Two
        {0, 2, 3, 5, 6},  # Three
        {1, 2, 3, 5},  # Four
        {0, 1, 3, 5, 6},  # Five
        {0, 1, 3, 4, 5, 6},  # Six
        {0, 2, 5},  # Seven
        {0, 1, 2, 3, 4, 5, 6},  # Eight
        {0, 1, 2, 3, 5, 6},  # Nine
    )

    total = 0
    all_digits, input_digits = parse_input(data)
    for all_digit_row, input_row in zip(all_digits, input_digits):
        for permutation in permutations(range(7), 7):
            for digit_word in all_digit_row:
                digit_set = get_set_from_word(permutation, digit_word)
                if digit_set not in digit_sets:
                    # Invalid digit found. On to the next permutation.
                    break
            else:
                number = 0
                for digit_word in input_row:
                    digit_set = get_set_from_word(permutation, digit_word)
                    digit = digit_sets.index(digit_set)
                    number = number * 10 + digit

                total += number
                break  # Found the number. Onto the next row.

    return total


test_data = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


def test_part1() -> None:
    assert part1(test_data) == 26


def test_part2() -> None:
    assert part2(test_data) == 61229


def main() -> None:
    with open(os.path.join(os.path.dirname(__file__), "input")) as file:
        data = file.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
