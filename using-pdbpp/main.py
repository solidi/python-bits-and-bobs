import random

MAX = 100


def main(num_loops=1000):
    for i in range(num_loops):
        num = random.randint(0, MAX)
        denom = random.randint(0, MAX)
        result = num / denom
        print("{} divided by {} is {:.2f}".format(num, denom, result))


if __name__ == "__main__":
    import sys
    arg = sys.argv[-1]
    if arg.isdigit():
        main(arg)
    else:
        main()
