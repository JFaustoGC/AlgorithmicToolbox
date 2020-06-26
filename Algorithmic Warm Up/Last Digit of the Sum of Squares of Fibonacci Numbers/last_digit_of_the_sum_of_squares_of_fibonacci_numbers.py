# python3


def last_digit_of_fibonacci_number(n):
    # assert 0 <= n <= 10 ** 18

    seq = "011235831459437077415617853819099875279651673033695493257291"
    num = [int(c) for c in seq]
    return num[n % 60]


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    # assert 0 <= n <= 10 ** 18

    h = last_digit_of_fibonacci_number(n)
    b = h + last_digit_of_fibonacci_number(n - 1)
    return (b * h) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
