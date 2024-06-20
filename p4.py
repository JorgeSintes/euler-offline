def is_pal(number: int) -> bool:
    number_str = str(number)
    for i in range(len(number_str) // 2):
        if number_str[i] != number_str[-1 - i]:
            return False
    return True


def largest_pal(num_digits: int) -> int:
    starting_point = 10**num_digits - 1
    largest = 0

    for i in range(starting_point, 0, -1):
        if i * i < largest:
            break
        for j in range(i, 0, -1):
            num = i * j
            if is_pal(num) and num > largest:
                largest = num

    return largest


if __name__ == "__main__":
    print(largest_pal(3))
