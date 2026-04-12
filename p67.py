from p18 import solve


def parse_triangle(input_path: str):
    with open(input_path, "r") as f:
        return [[int(num) for num in line.split()] for line in f.readlines() if line]


if __name__ == "__main__":
    triangle = parse_triangle("p67.txt")
    solution = solve(triangle)
    print(max(solution[-1]))
