#!/bin/python

ROWS = 140
COLS = 140


"""
  0123456789
0 467..114..
1 ...*......
2 ..35..633.
3 ......#...
4 617*......
5 .....+.58.
6 ..592.....
7 ......755.
8 ...$.*....
9 .664.598..
"""


class PartNumber:
    def __init__(self, value, positions):
        self.value = value
        self.positions = positions
        self.hasAdjacentSymbol = False


class Symbol:
    def __init__(self, value, position):
        self.value = value
        self.position = (position)
        self.adjs = []

    def add_adjacent(self, adj_position):
        self.adjs.append(adj_position)


symbols = []
part_numbers = []


def main():
    print("#################")
    grid = []

    # with open("data1.txt", "r") as f:
    with open("data.txt", "r") as f:
        for d in f.readlines():
            grid.append(list(d))

    in_numb = False
    cur_numb = ""
    cur_pos = []

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c].isdigit():
                in_numb = True
                cur_numb = cur_numb + grid[r][c]
                cur_pos.append((c, r))
                continue

            if grid[r][c] == ".":
                if in_numb:
                    in_numb = False
                    part_numbers.append(PartNumber(cur_numb, cur_pos))
                    cur_numb = ""
                    cur_pos = []
                continue

            if is_symbol(grid[r][c]):
                if in_numb:
                    in_numb = False
                    part_numbers.append(PartNumber(cur_numb, cur_pos))
                    cur_numb = ""
                    cur_pos = []

                s = Symbol(grid[r][c], (c, r))
                adjs = get_adjs(s.position)
                for adj in adjs:
                    x = adj[0]
                    y = adj[1]
                    if grid[y][x].isdigit():
                        s.add_adjacent((x, y))
                symbols.append(s)

    for pn in part_numbers:
        for pos in pn.positions:
            for symbol in symbols:
                if pos in symbol.adjs:
                    pn.hasAdjacentSymbol = True

    sum2 = 0
    for sym in symbols:
        seen_values = []
        matches = []
        if sym.value != "*":
            continue
        for pn in part_numbers:
            for sym_adjs in sym.adjs:
                if sym_adjs in pn.positions:
                    if pn.value not in seen_values:
                        seen_values.append(pn.value)
                        matches.append(pn)
        if len(matches) == 2:
            sum2 += int(matches[0].value) * int(matches[1].value)

    sum1 = 0
    for pn in part_numbers:
        if pn.hasAdjacentSymbol:
            sum1 += int(pn.value)

    print("part1:", sum1)
    print("part2:", sum2)


def is_symbol(s):
    symbols = "!@#$%^&*()_+-=/"
    if s in symbols:
        return True
    return False


def get_adjs(xy):
    res = []
    res.append(adj_top_left(xy[0], xy[1]))
    res.append(adj_top_center(xy[0], xy[1]))
    res.append(adj_top_right(xy[0], xy[1]))
    res.append(adj_right(xy[0], xy[1]))
    res.append(adj_bottom_right(xy[0], xy[1]))
    res.append(adj_bottom_center(xy[0], xy[1]))
    res.append(adj_bottom_left(xy[0], xy[1]))
    res.append(adj_left(xy[0], xy[1]))

    result = []

    for r in res:
        if r[0] != -1 and r[1] != -1:
            result.append(r)
    return result


def adj_top_left(x, y):
    if x == 0 or x >= COLS:
        return (-1, -1)
    if y == 0:
        return (-1, -1)
    return (x - 1, y - 1)


def adj_top_center(x, y):
    if y == 0:
        return (-1, -1)
    return (x, y - 1)


def adj_top_right(x, y):
    if y == 0:
        return (-1, -1)
    if x >= COLS-1:
        return (-1, -1)
    return (x + 1, y - 1)


def adj_right(x, y):
    if x >= COLS-1:
        return (-1, -1)
    return (x + 1, y)


def adj_bottom_right(x, y):
    if y >= ROWS-1:
        return (-1, -1)
    return (x + 1, y + 1)


def adj_bottom_center(x, y):
    if y >= ROWS-1:
        return (-1, -1)
    return (x, y + 1)


def adj_bottom_left(x, y):
    if y >= ROWS-1:
        return (-1, -1)
    return (x - 1, y + 1)


def adj_left(x, y):
    if x == 0:
        return (-1, -1)
    return (x - 1, y)


if __name__ == "__main__":
    main()
