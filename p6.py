def sum_squares(numbers: int) -> int:
    sum = 0
    for i in range(1, numbers + 1):
        sum += i**2
    return sum


def square_sum(numbers: int) -> int:
    return ((numbers + 1) * numbers // 2) ** 2


def solve(n: int) -> int:
    return square_sum(n) - sum_squares(n)


if __name__ == "__main__":
    print(solve(100))
