#!/usr/bin/env python3

import sys
from collections import defaultdict

from picotui.widgets import *
from picotui.menu import *
from picotui.context import Context


def main():
    words = [l.strip() for l in open(sys.argv[1]).read().split("\n")]
    word_3 = defaultdict(list)
    for w in words:
        word_3[w[:3]].append(w)

    trim_y = set(
        [l.strip() for l in open("trim_y.txt").read().strip().split("\n")]
    )
    trim_n = set(
        [l.strip() for l in open("trim_n.txt").read().strip().split("\n")]
    )

    try:
        for c3, c3words in word_3.items():
            if any(w in trim_y or w in trim_n for w in c3words):
                continue

            with Context():
                d = Dialog(1, 1)
                l = ["None"] + c3words
                lb = WListBox(max(len(x) for x in l), min(10, len(l)), l)
                d.autosize()
                # lb.autosize()
                lb.finish_dialog = ACTION_OK
                d.add(1, 1, lb)
                res = d.loop()
            if res != ACTION_OK:
                break

            # print(lb.choice)
            # print(c3words)
            if lb.choice == 0:
                trim_n |= set(c3words)
            else:
                trim_y.add(c3words[lb.choice - 1])
                trim_n |= set(c3words) - set(c3words[lb.choice - 1])
    finally:
        with open("trim_y.txt", "w") as t:
            t.write("\n".join(sorted(trim_y)) + "\n")
        with open("trim_n.txt", "w") as t:
            t.write("\n".join(sorted(trim_n)) + "\n")


if __name__ == "__main__":
    main()
