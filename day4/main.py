#!/bin/python

import re


def main():

    pattern = r"\b\d{1,2}\b"

    val = 0
    with open("data.txt") as f:
        data = f.read()
        for d in data.split("\n"):
            dd = d.split(":")
            ddd = dd[1].split("|")
            first = re.findall(pattern, ddd[0])
            second = re.findall(pattern, ddd[1])

            match_count = 0
            for s in second:
                if s in first:
                    match_count += 1
            if match_count > 0:
                val += 2 ** (match_count-1)

    print(val)


if __name__ == "__main__":
    main()
