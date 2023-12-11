#!/bin/python3

import re

def main():
    total1 = 0
    total2 = 0
    pattern1 = re.compile(r'[0-9]')
    pattern2 = re.compile(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))')

    with open('data.txt', 'r') as f:
        lines = f.readlines()
        for line in lines: 
            
            numbers = re.findall(pattern1, line)
            first = numbers[0]
            last = numbers[-1]
            total1 += int(str(first) + str(last))

            matches = re.findall(pattern2, line)
            first2 = word_to_int(matches[0])
            last2 = word_to_int(matches[-1])

            total2 += int(str(first2) + str(last2))
    
    print("total1:", total1)
    print("total2:", total2)


def word_to_int(s):
    s = s.replace("one", "1")
    s = s.replace("two", "2")
    s = s.replace("three", "3")
    s = s.replace("four", "4")
    s = s.replace("five", "5")
    s = s.replace("six", "6")
    s = s.replace("seven", "7")
    s = s.replace("eight", "8")
    s = s.replace("nine", "9")
    return int(s)


if __name__ == '__main__':
    main()
