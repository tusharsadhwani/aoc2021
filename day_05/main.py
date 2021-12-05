"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These
vents constantly produce large, opaque clouds, so it would be best to
avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of
nearby lines of vents (your puzzle input) for you to review. For
example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 ->
x2,y2 where x1,y1 are the coordinates of one end the line segment and
x2,y2 are the coordinates of the other end. These line segments include
the points at both ends. In other words:

- An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
- An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either
x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce
the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner
is 9,9. Each position is shown as the number of lines which cover that
point or . if no line covers that point. The top-left pair of 1s, for
example, comes from 2,2 -> 2,1; the very bottom row is formed by the
overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of
points where at least two lines overlap. In the above example, this is
anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at
least two lines overlap?
"""
import os
from collections import defaultdict
from typing import DefaultDict

Points = DefaultDict[tuple[int, int], int]


def parse_data(data: str) -> Points:
    points: Points = defaultdict(int)
    for line in data.splitlines():
        x1, y1, x2, y2 = (
            int(num) for coords in line.split("->") for num in coords.split(",")
        )
        if x1 != x2 and y1 != y2:
            continue

        if x1 == x2:
            # min and max, to get the smaller number into y1
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                points[x1, y] += 1

        elif y1 == y2:
            # min and max, to get the smaller number into x1
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                points[x, y1] += 1

    return points


def part1(data: str) -> int:
    points = parse_data(data)
    return len([count for count in points.values() if count >= 2])


def part2(data: str) -> None:
    ...


test_data = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def test_part1() -> None:
    assert part1(test_data) == 5


def test_part2() -> None:
    assert part2(test_data) == ...


def main() -> None:
    with open(os.path.join(os.path.dirname(__file__), "input")) as file:
        data = file.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
