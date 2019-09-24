#!/usr/bin/env python3

import sys


def main():
    left_hand = set("qwertasdfgzxcvb")

    alls = {}
    lefts = []
    rights = []

    with open(sys.argv[1]) as words:
        for word in map(str.strip, words):
            if len(word) < 3:
                continue
            hands = [c in left_hand for c in word[:3]]

            if hands[0] != hands[1] and hands[0] == hands[2]:
                # todo don't skip, choose best
                # if word[:3] in alls:
                #     continue
                alls[word[:3]] = True

                if hands[0]:
                    lefts.append(word)
                else:
                    rights.append(word)

    print(len(lefts), len(rights))

    with open("left" + sys.argv[1], "w") as f:
        f.write("\n".join(lefts))
    with open("right" + sys.argv[1], "w") as f:
        f.write("\n".join(rights))


if __name__ == "__main__":
    main()
