from dataclasses import dataclass

from p3 import factorize


@dataclass
class Factorization:
    factors: list[int]
    indeces: dict[int, int]

    @classmethod
    def from_factorization(cls, factorization: list[int]):
        factors = list[int]()
        indeces = dict[int, int]()

        for f in factorization:
            if f not in factors:
                factors.append(f)
                indeces[f] = 1
            else:
                indeces[f] += 1

        return cls(factors, indeces)

    @classmethod
    def from_number(cls, number: int):
        return cls.from_factorization(factorize(number))

    @property
    def num_divisors(self) -> int:
        result = 1
        for i in self.indeces.values():
            result *= i + 1

        return result


if __name__ == "__main__":
    triangular = 3
    i = 2
    f = Factorization.from_number(triangular)
    while f.num_divisors < 500:
        i += 1
        triangular += i
        f = Factorization.from_number(triangular)

    print(triangular)
