def main():
    # type: () -> None
    print(gcd(15, 10))
    print(gcd(45, 12))


def gcd(a, b):
    # type: (int, int) -> int
    while b:
        a, b = b, a%b
    return a
