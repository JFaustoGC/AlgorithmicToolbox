# python3


def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
