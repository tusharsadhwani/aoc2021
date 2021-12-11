"""
--- Day 10: Syntax Scoring ---
You ask the submarine to determine the best route out of the deep-sea
cave, but it only replies:

Syntax error in navigation subsystem on line: all of them

All of them?! The damage is worse than you thought. You bring up a copy
of the navigation subsystem (your puzzle input).

The navigation subsystem syntax is made of several lines containing
chunks. There are one or more chunks on each line, and chunks contain
zero or more other chunks. Adjacent chunks are not separated by any
delimiter; if one chunk stops, the next chunk (if any) can immediately
start. Every chunk must open and close with one of four legal pairs of
matching characters:

- If a chunk opens with (, it must close with ).
- If a chunk opens with [, it must close with ].
- If a chunk opens with {, it must close with }.
- If a chunk opens with <, it must close with >.

So, () is a legal chunk that contains no other chunks, as is []. More
complex but valid chunks include ([]), {()()()}, <([{}])>,
[<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard
the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character -
that is, where the characters it opens and closes with do not form one
of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and
<([]){()}[{}]). Such a chunk can appear anywhere within a line, and its
presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]

Some of the lines aren't corrupted, just incomplete; you can ignore
these lines for now. The remaining five lines are corrupted:

- {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
- [[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
- [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
- [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
- <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.

Stop at the first incorrect closing character on each corrupted line.

Did you know that syntax checkers actually have contests to see who can
get the high score for syntax errors in a file? It's true! To calculate
the syntax error score for a line, take the first illegal character on
the line and look it up in the following table:

- ): 3 points.
- ]: 57 points.
- }: 1197 points.
- >: 25137 points.

In the above example, an illegal ) was found twice (2*3 = 6 points), an
illegal ] was found once (57 points), an illegal } was found once (1197
points), and an illegal > was found once (25137 points). So, the total
syntax error score for this file is 6+57+1197+25137 = 26397 points!

Find the first illegal character in each corrupted line of the
navigation subsystem. What is the total syntax error score for those
errors?
"""
import os


def get_illegal_index(line: str) -> int:
    """
    Returns the index at which brackets don't align anymore.
    If all brackets match, return -1.
    """
    stack: list[str] = []
    opening_map = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    for index, bracket in enumerate(line):
        if bracket in "([{<":
            stack.append(bracket)
            continue

        opening_bracket = opening_map[bracket]
        if stack.pop() != opening_bracket:
            return index

    # TODO: what if opening brackets left in the stack.
    # Will probably have to deal with in part 2.
    return -1


def part1(data: str) -> int:
    illegal_scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    total_score = 0
    for line in data.splitlines():
        index = get_illegal_index(line)
        if index == -1:
            continue

        bracket = line[index]
        total_score += illegal_scores[bracket]

    return total_score


def part2(data: str) -> None:
    ...


test_data = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


def test_part1() -> None:
    assert part1(test_data) == 26397


def test_part2() -> None:
    assert part2(test_data) == ...


def main() -> None:
    with open(os.path.join(os.path.dirname(__file__), "input")) as file:
        data = file.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
