import random

def generate_unique_values():
    # We set -100 as the lower bound for computation purposes
    x = random.randint(-18, -5)  # -18 <= x <= -5
    y = random.randint(-100, -18)  # y <= -18
    z = random.randint(-100, 4)  # z < 5

    # If any two values are the same, call the function recursively
    if x == y or y == z or x == z:
        return generate_unique_values()
    else:
        return x, y, z

def find_solutions(N):
    solutions = []
    for _ in range(N):
        x, y, z = generate_unique_values()
        solutions.append((x, y, z))
    return solutions

# Number of solutions you want to generate
N = 10  # for example, change to your preference

solutions = find_solutions(N)
for i, solution in enumerate(solutions, 1):
    print(f"Solution {i}: x={solution[0]}, y={solution[1]}, z={solution[2]}")
