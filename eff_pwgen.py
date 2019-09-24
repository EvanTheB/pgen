import random
import math
import argparse

r = random.SystemRandom()


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
    p = get_password(this_list, num=args.number)
    print(" ".join(p))
    print("".join(s[:3] for s in p))
    bits(this_list, num=args.number)


if __name__ == "__main__":
    main()
