# python3


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x, y = 0, 1
        for i in range(n - 1):
            z = (x + y) % 10
            x, y = y, z
        return z


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
