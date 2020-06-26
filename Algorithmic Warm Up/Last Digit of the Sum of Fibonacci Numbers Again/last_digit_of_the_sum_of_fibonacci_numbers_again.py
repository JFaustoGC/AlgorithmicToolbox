# python3

def sum_to(n):
    # assert 0 <= n <= 10 ** 18

    seq = "011235831459437077415617853819099875279651673033695493257291"
    num = [int(c) for c in seq]
    return (sum(num) * (n // 60) + sum(num[:(n % 60) + 1]))


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    # assert 0 <= from_index <= to_index <= 10 ** 18
    seq = "011235831459437077415617853819099875279651673033695493257291"
    num = [int(c) for c in seq]
    if from_index == to_index:
        return num[from_index % 60]
    else:
        return  (sum_to(to_index) - sum_to(from_index - 1)) % 10

if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
