"""
Recursively run Havel-Hakimi until a solution is reached
This function runs the algorithm reversed from what is usually taught (sorts ascending),
but prints the reverse of the secuences so they can be easyly interpreted
"""
def havel_hakimi(seq):
    # if seq is empty or only contains zeros,
    # degree sequence is valid
    if len(seq) < 1 or all(deg == 0 for deg in seq):
        print("Se puede construir un grafo con esta secuencia\n")
        return True

    print(list(reversed(seq)), end="")
    seq.sort()
    print(" --ordenar--> ", end="")
    print(list(reversed(seq)))

    last = seq[len(seq)-1]
    if last > len(seq)-1:
        print("\nNo se puede construir un grafo con esta secuencia.\n")
        return False

    print(list(reversed(seq)), end="")

    # remove last element
    seq.remove(last)

    # iterate seq backwards
    for num in range(len(seq)-1, len(seq)-last-1, -1):
        if seq[num] > 0:
            seq[num] -= 1
        else:
            print("\nNo se puede construir un grafo con esta secuencia\n")
            return False

    print(" --alg-->", end="")
    print(list(reversed(seq)))

    # recursive call
    return havel_hakimi(seq)

if __name__ == "__main__":
    havel_hakimi([7, 3, 3, 6, 6, 2, 2, 2, 1])
    havel_hakimi([5, 4, 4, 6, 6, 2, 2, 2, 1])
    havel_hakimi([3, 5, 5, 6, 6, 2, 2, 2, 1])
    havel_hakimi([1, 6, 6, 6, 6, 2, 2, 2, 1])