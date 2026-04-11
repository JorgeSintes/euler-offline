COLLATZ_CACHE = dict[int, int]()


def collatz(n: int):
    i = 1
    nums = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        if n in COLLATZ_CACHE:
            # print(nums)
            for idx, number in enumerate(nums):
                COLLATZ_CACHE[number] = i + COLLATZ_CACHE[n] - idx
            return i + COLLATZ_CACHE[n]

        i += 1
        nums.append(n)

    for idx, number in enumerate(nums):
        COLLATZ_CACHE[number] = i - idx

    # print(nums)
    return i


if __name__ == "__main__":
    max = 0
    max_num = 0
    for i in range(2, 1_000_000):
        col = collatz(i)
        # if i % 10 == 0:
        #     print(f"{i}: {col}")
        if col > max:
            max = col
            max_num = i

    print(max_num)
