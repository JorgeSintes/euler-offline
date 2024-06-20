def factorize(number: int) -> list[int]:
    prime_fac = []
    f = 2
    while f * f <= number:
        if number % f == 0:
            prime_fac.append(f)
            number = number // f
        else:
            f += 1 if f == 2 else 2

    if number != -1:
        prime_fac.append(number)

    return prime_fac


if __name__ == "__main__":
    # print(factorize(13195))
    print(factorize(2520))
    # print(factorize(600851475143)[-1])
