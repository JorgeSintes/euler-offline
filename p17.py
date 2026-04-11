NUMBER_MAP = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "one thousand",
}


def write_number(n: int) -> str:
    if n in NUMBER_MAP:
        return NUMBER_MAP[n]

    return_str = ""

    centena = n // 100 % 10
    decena = n // 10 % 10
    unidad = n % 10

    if centena:
        return_str += f"{NUMBER_MAP[centena]} hundred"
        if decena or unidad:
            return_str += " and "

    if decena * 10 + unidad in NUMBER_MAP:
        return return_str + f"{NUMBER_MAP[decena * 10 + unidad]}"

    if decena:
        return_str += f"{NUMBER_MAP[decena * 10]}-"
    if unidad:
        return_str += f"{NUMBER_MAP[unidad]}"

    return return_str


def count_len(n: str) -> int:
    return len(n.lstrip().rstrip()) - n.count(" ") - n.count("-")


if __name__ == "__main__":
    total = 0
    for i in range(1, 1001):
        num = write_number(i)
        total += count_len(num)

    print(total)
