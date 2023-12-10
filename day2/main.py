#!/bin/python3

import re

MAX_AVAILABLE = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def main():
    sum_valid_games = 0
    sum_game_powers = 0

    # with open("data1.txt", "r") as f:
    with open("data.txt", "r") as f:
        all_games = f.readlines()

        for game in all_games:
            min_needed = {
                "red": [0],
                "green": [0],
                "blue": [0]
            }

            this_game_power = 0
            is_possible_game = True

            game_id = game_id(game)
            game_data = game_data(game)
            game_rounds = game_data.split(';')

            for round_id in range(0, len(game_rounds)):
                cube_data = game_rounds[round_id].split(',')
                for cube_entry in cube_data:
                    val = cube_entry.split()

                    cubes_per_color = {}
                    cubes_per_color[val[1]] = val[0]

                    for k, v in cubes_per_color.items():
                        min_needed[k].append(int(v))
                        if k in MAX_AVAILABLE.keys():
                            if int(v) > MAX_AVAILABLE[k]:
                                is_possible_game = False
                        else:
                            is_possible_game = False
            if is_possible_game:
                sum_valid_games += int(game_id)

            this_game_power = max(
                min_needed["red"]) * max(min_needed["green"]) * max(min_needed["blue"])

            sum_game_powers += this_game_power
    print("Total:", sum_valid_games)
    print("all_game_power:", sum_game_powers)


def game_data(line):
    return line.split(':')[-1]


def game_id(line):
    g = line.split(':')[0]
    return g.split()[-1]


if __name__ == "__main__":
    main()
