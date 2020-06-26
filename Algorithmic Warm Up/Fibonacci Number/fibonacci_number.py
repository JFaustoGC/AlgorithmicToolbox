# python3


def fibonacci_number(n):
    assert 0 <= n <= 45

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x, y = 0, 1
        for i in range(n - 1):
            z = x + y
            x, y = y, z
        return z


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_number(n))
