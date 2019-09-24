#!/usr/bin/env python3

import sys
from collections import defaultdict


class Getch:
    # https://stackoverflow.com/a/510364/3936601
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def main():
    words = [l.strip() for l in open(sys.argv[1]).read().split("\n")]
    word_3 = defaultdict(list)
    for w in words:
        word_3[w[:3]].append(w)

    trim_y = set([l.strip() for l in open("trim_y.txt").read().strip().split("\n")])
    trim_n = set([l.strip() for l in open("trim_n.txt").read().strip().split("\n")])

    exits = set('\x03\x1c\x04')
    getc = Getch()
    for w in words:
        if w in trim_y or w in trim_n:
            continue

        print(w)
        c = getc()

        if c in exits:
            break

        if c == "y":
            trim_y.add(w)
        else:
            trim_n.add(w)

    with open("trim_y.txt", 'w') as t:
        t.write("\n".join(sorted(trim_y)) + "\n")
    with open("trim_n.txt", 'w') as t:
        t.write("\n".join(sorted(trim_n)) + "\n")


if __name__ == "__main__":
    main()
