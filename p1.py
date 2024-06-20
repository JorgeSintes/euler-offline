from typing import Tuple


def is_multiple(num: int, divisor: int) -> bool:
    return num % divisor == 0


def solve(cap: int, divisors: Tuple[int, int]):
    if 2 in divisors:
        sum = 2
    else:
        sum = 0

    for num in range(3, cap):
        if is_multiple(num, divisors[0]) or is_multiple(num, divisors[1]):
            sum += num

    return sum


if __name__ == "__main__":
    print(solve(1000, (3, 5)))
