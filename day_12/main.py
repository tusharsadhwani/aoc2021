r"""
--- Day 12: Passage Pathing ---
With your submarine's subterranean subsystems subsisting suboptimally,
the only way you're getting out of this cave anytime soon is by finding
a path yourself. Not just a path - the only way to know if you've found
the best path is to find all of them.

Fortunately, the sensors are still mostly working, and so you build a
rough map of the remaining caves (your puzzle input). For example:

start-A
start-b
A-c
A-b
b-d
A-end
b-end

This is a list of how all of the caves are connected. You start in the
cave named start, and your destination is the cave named end. An entry
like b-d means that cave b is connected to cave d - that is, you can
move between them.

So, the above cave system looks roughly like this:

    start
    /   \
c--A-----b--d
    \   /
     end

Your goal is to find the number of distinct paths that start at start,
end at end, and don't visit small caves more than once. There are two
types of caves: big caves (written in uppercase, like A) and small caves
(written in lowercase, like b). It would be a waste of time to visit any
small cave more than once, but big caves are large enough that it might
be worth visiting them multiple times. So, all paths you find should
visit small caves at most once, and can visit big caves any number of
times.

Given these rules, there are 10 paths through this example cave system:

start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end

(Each line in the above list corresponds to a single path; the caves
visited by that path are listed in the order they are visited and
separated by commas.)

Note that in this cave system, cave d is never visited by any path: to
do so, cave b would need to be visited twice (once on the way to cave d
and a second time when returning from cave d), and since cave b is
small, this is not allowed.

Here is a slightly larger example:

dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc

The 19 paths through it are as follows:

start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end

Finally, this even larger example has 226 paths through it:

fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW

How many paths through this cave system are there that visit small caves
at most once?
"""
import os
from collections import defaultdict
from typing import Callable, DefaultDict, Optional, Tuple, Union

Graph = DefaultDict[str, set[str]]
Path = Tuple[str, ...]
num = Union[int, float]


def parse_data(data: str) -> Graph:
    """Returns an adjacency list of the graph data."""
    graph: Graph = defaultdict(set)

    for line in data.splitlines():
        start, end = line.split("-")
        graph[start].add(end)
        graph[end].add(start)

    return graph


def get_cave_visit_count(
    cave: str,
    small_cave_visits: num,
    big_cave_visits: num,
) -> num:
    """Returns how many times you can visit a cave"""
    return big_cave_visits if cave.isupper() else small_cave_visits


def _depth_first_search(
    graph: Graph,
    paths: list[Path],
    point: str,
    cave_visits_left: dict[str, num],
    current_path: Optional[Path] = None,
) -> None:
    if current_path is None:
        current_path = (point,)

    for cave in graph[point]:
        if cave == "start":
            continue

        if cave == "end":
            final_path = (*current_path, "end")
            paths.append(final_path)
            continue

        if cave_visits_left[cave] >= 1:
            cave_visits_left_copy = cave_visits_left.copy()
            cave_visits_left_copy[cave] -= 1

            new_path = (*current_path, cave)
            _depth_first_search(
                graph,
                paths,
                cave,
                cave_visits_left_copy,
                new_path,
            )


def find_paths(graph: Graph, small_cave_visits: num, big_cave_visits: num) -> int:
    """Find all paths from `start` to `end` within given constraints."""
    paths: list[Path] = []
    starting_point = "start"

    cave_visits_left: dict[str, num] = {}
    cave_visits_left.update(
        {
            cave: get_cave_visit_count(
                cave,
                small_cave_visits,
                big_cave_visits,
            )
            for cave in graph
        }
    )
    cave_visits_left.pop("start")
    _depth_first_search(
        graph,
        paths,
        starting_point,
        cave_visits_left,
    )
    return len(paths)


def part1(data: str) -> int:
    graph = parse_data(data)

    small_cave_visits = 1
    big_cave_visits = float("inf")

    path_count = find_paths(graph, small_cave_visits, big_cave_visits)
    return path_count


def part2(data: str) -> None:
    ...


test_data = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

part1_simple_1 = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

part1_simple_2 = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""


def test_part1() -> None:
    assert part1(part1_simple_1) == 10
    assert part1(part1_simple_2) == 19
    assert part1(test_data) == 226


def test_part2() -> None:
    assert part2(test_data) == ...


def main() -> None:
    with open(os.path.join(os.path.dirname(__file__), "input")) as file:
        data = file.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
