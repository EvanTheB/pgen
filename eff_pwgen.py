import random
import math
import argparse
from itertools import chain

r = random.SystemRandom()


def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


def get_alt_password(this_list, num=6, max_len=None):
    left_hand = set("qwertasdfgzxcvb")

    left_right = [[], []]
    left_only = []

    for w in this_list:
        if w[0] in left_hand and w[1] not in left_hand and w[2] in left_hand:
            left_right[0].append(w)
        elif (
            w[0] not in left_hand
            and w[1] in left_hand
            and w[2] not in left_hand
        ):
            left_right[1].append(w)

        if all(c in left_hand for c in w[:3]):
            left_only.append(w)

    print("left", len(left_right[0]))
    print("right", len(left_right[1]))
    print("left_only", len(left_only[1]))

    return list(
        flatten(
            [
                (r.choice(left_right[0]), r.choice(left_right[1]))
                for _ in range(num // 2)
            ]
        )
    )


def get_password(this_list, num=6, max_len=None):
    # try, but not forever
    for i in range(1000):
        my_password = [r.choice(this_list) for _ in range(num)]
        if max_len is None or len(" ".join(my_password)) < max_len:
            return my_password
    else:
        raise Exception("Could not find a password")


def bits(this_list, num=6, max_len=None):
    if max_len is None:
        print("words:", math.log(len(this_list) ** num) / math.log(2))
        print(
            "chars:",
            math.log(24 ** (num * len(min(this_list, key=lambda s: len(s)))))
            / math.log(2),
        )
        print("3chars:", math.log(24 ** (3 * num)) / math.log(2))


def main():
    parser = argparse.ArgumentParser(description="Get a password")
    parser.add_argument(
        "number",
        type=int,
        default=6,
        nargs="?",
        help="number of words in password",
    )
    parser.add_argument(
        "wordlist",
        type=argparse.FileType("r"),
        nargs="?",
        default="eff_large_wordlist.txt",
        help="a wordlist",
    )
    args = parser.parse_args()

    this_list = args.wordlist.read().strip().split()[1::2]

    p = get_alt_password(this_list, num=args.number)
    print(" ".join(p))
    print("".join(s[:3] for s in p))
    bits(this_list, num=args.number)


if __name__ == "__main__":
    main()
