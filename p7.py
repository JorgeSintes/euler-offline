def is_prime(number: int, primes: list[int]) -> bool:
    for prime in primes:
        if number % prime == 0:
            return False
        if prime * prime > number:
            break  # early stop

    return True


def find_primes(n: int) -> list[int]:
    """
    Returns a list with the n first primes.
    """
    primes = [2]
    i = 3
    while len(primes) < n:
        if is_prime(i, primes):
            primes.append(i)

        i += 2

    return primes


if __name__ == "__main__":
    print(find_primes(10001)[-1])
