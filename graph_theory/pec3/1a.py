def two(a, b, c):
    return (not a or not b) and (c or not b)

def three(a, b, c):
    return (not a or not b or c) and (c or not b) and a

def five(a, b, c):
    return (not b or a or c) and (c or not b or a)

n_vars = 3

def print_table():
    print(f'{"a":>2} {"b":>2} {"c":>2} {"two":>4} {"three":>6} {"five":>4}')
    for i in range(2 ** n_vars):
        a = i & 1
        b = (i >> 1) & 1
        c = (i >> 2) & 1
        print(f'{a:>2} {b:>2} {c:>2} {two(a, b, c):>4} {three(a, b, c):>6} {five(a, b, c):>4}')

if __name__ == '__main__':
    print_table()