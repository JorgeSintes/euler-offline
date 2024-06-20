import timeit


def fib_rec(n: int):
    if n == 0:
        return 1
    if n == 1:
        return 2

    return fib_rec(n - 1) + fib_rec(n - 2)


class Fib:
    def __init__(self):
        self._cache = {
            0: 1,
            1: 2,
        }

    def get(self, n: int):
        if n == 0:
            return 1
        if n == 1:
            return 2

        if n in self._cache.keys():
            return self._cache[n]

        calc = self.get(n - 1) + self.get(n - 2)
        self._cache[n] = calc

        return calc


def solve_rec():
    last_fib = 0
    i = 0
    res = 0
    while last_fib < 4e6:
        if last_fib % 2 == 0:
            res += last_fib
        last_fib = fib_rec(i)
        i += 1

    print(res)


def solve():
    fib = Fib()
    last_fib = 0
    i = 0
    res = 0
    while last_fib < 4e6:
        if last_fib % 2 == 0:
            res += last_fib
        last_fib = fib.get(i)
        i += 1

    print(res)


if __name__ == "__main__":
    print(timeit.Timer(solve_rec).repeat(repeat=5, number=1))
    print(timeit.Timer(solve).repeat(repeat=5, number=1))
    solve()
