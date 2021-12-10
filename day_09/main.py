"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically
active; small hydrothermal vents release smoke into the caves that
slowly settles like rain.

If you can model how the smoke flows through the caves, you might be
able to avoid it and be that much safer. The submarine generates a
heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example,
consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9
is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower
than any of its adjacent locations. Most locations have four adjacent
locations (up, down, left, and right); locations on the edge or corner
of the map have three or two adjacent locations, respectively. (Diagonal
locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two
are in the first row (a 1 and a 0), one is in the third row (a 5), and
one is in the bottom row (also a 5). All other locations on the
heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above
example, the risk levels of the low points are 2, 1, 6, and 6. The sum
of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the
risk levels of all low points on your heightmap?

--- Part Two ---
Next, you need to find the largest basins so you know what areas are
most important to avoid.

A basin is all locations that eventually flow downward to a single low
point. Therefore, every low point has a basin, although some basins are
very small. Locations of height 9 do not count as being in any basin,
and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin,
including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210    21........
3987894921    3.........
9856789892 => ..........
8767896789    ..........
9899965678    ..........

The top-right basin, size 9:

2199943210    .....43210
3987894921    ......4.21
9856789892 => .........2
8767896789    ..........
9899965678    ..........

The middle basin, size 14:

2199943210    ..........
3987894921    ..878.....
9856789892 => .85678....
8767896789    87678.....
9899965678    .8........

The bottom-right basin, size 9:

2199943210    ..........
3987894921    ..........
9856789892 => .......8..
8767896789    ......678.
9899965678    .....65678

Find the three largest basins and multiply their sizes together. In the
above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest
basins?
"""
import os


def parse_data(data: str) -> list[list[int]]:
    return [[int(char) for char in line] for line in data.splitlines()]


def is_low_point(grid: list[list[int]], x: int, y: int) -> bool:
    value = grid[x][y]

    neighbours = []
    if x > 0:
        neighbours.append(grid[x - 1][y])
    if x + 1 < len(grid):
        neighbours.append(grid[x + 1][y])

    if y > 0:
        neighbours.append(grid[x][y - 1])
    if y + 1 < len(grid[0]):
        neighbours.append(grid[x][y + 1])

    if all(neighbour > value for neighbour in neighbours):
        return True

    return False


def part1(data: str) -> int:
    grid = parse_data(data)

    risk_level_sum = 0
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if is_low_point(grid, x, y):
                risk_level = cell + 1
                risk_level_sum += risk_level

    return risk_level_sum


def part2(data: str) -> int:
    ...


test_data = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def test_part1() -> None:
    assert part1(test_data) == 15


def test_part2() -> None:
    assert part2(test_data) == 


def main() -> None:
    with open(os.path.join(os.path.dirname(__file__), "input")) as file:
        data = file.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
