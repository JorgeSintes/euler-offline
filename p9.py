def solve_naive(num: int) -> int:
    max_try = num // 2

    for i in range(1, max_try):
        for j in range(i, max_try):
            k = num - i - j
            if k * k == (i**2 + j**2):
                return int(i * j * k)

    return 0


if __name__ == "__main__":
    print(solve_naive(int(1000)))
