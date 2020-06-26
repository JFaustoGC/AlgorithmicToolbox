# python3


def fibonacci_number(n):
    assert 0 <= n <= 10 ** 4

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


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    sequence = ""
    i = 0
    while True:
        sequence += str(fibonacci_number(i) % m)
        if sequence[-3:] == "011" and i > 2:
            break
        i += 1
    return fibonacci_number(n % (i - 2 )) % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
