target = 2_000_000


def is_prime(n: int, primes: list[int]) -> bool:
    for p in primes:
        if n % p == 0:
            return False
        if p > n**0.5:
            return True

    return True


if __name__ == "__main__":
    primes = []
    sum = 0
    for i in range(2, target):
        if is_prime(i, primes):
            primes.append(i)
            sum += i

    print(sum)
