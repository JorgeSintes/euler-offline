def find_primes(number: int) -> list[int]:
    primes = [2]
    for i in range(3, number + 1, 2):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes


def factorize(number: int, primes: list[int]) -> dict[int, int]:
    prime_fac = {k: 0 for k in primes}

    i = 0
    while number != 1:
        if number % primes[i] == 0:
            prime_fac[primes[i]] += 1
            number = number // primes[i]
        else:
            i += 1

    return prime_fac


def smallest_evenly_divisible(top_number: int):
    sol = 1
    primes = find_primes(top_number)
    prime_fac = {k: 1 for k in primes}
    for num in range(2, top_number + 1):
        for k, v in factorize(num, primes).items():
            if prime_fac[k] < v:
                prime_fac[k] = v

    for k, v in prime_fac.items():
        sol *= k**v
    return sol


if __name__ == "__main__":
    print(smallest_evenly_divisible(20))
