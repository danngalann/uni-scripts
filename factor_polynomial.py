#!/usr/bin/python3

import sys

numbers = [int(x) for x in sys.argv[1:]]

def get_dividents(number):
    positives = [x for x in range(0, number if number > 0 else number * -11) if x != 0 and number % x == 0]
    negatives = [x for x in range(0, number if number < 0 else number * -1, -1) if x != 0 and number % x == 0]
    itself = [number, number * -1]

    return positives + negatives + itself

def ruffini(expression, independent_term):
    result = [None for _ in range(len(expression))]
    for index, number in enumerate(expression):
        if index == 0:
            result[0] = number
            continue

        result[index] = number + (result[index - 1] * independent_term)

    return result


def get_next_divident(expression):
    dividents = get_dividents(expression[-1])

    for divident in dividents:
        next_expression = ruffini(expression, divident)

        if (next_expression[-1] == 0):
            return divident, next_expression

    print("No divident was found for expression", expression)
    print("If the variable is elevated to an exponent, this expression may not have a solution.")
    exit()

dividents = []
expressions = []
def factor(expression):
    
    if (len(expression) == 1):
        print("Coeficients:", dividents)
        print("Result:", '*'.join([f"(x+{x * -1})" for x in dividents]), '' if expression[-1] == 1 else f'* {expression[-1]}')
        print()
        print("Result after each coeficient:")
        print(*expressions, sep="\n")
        return

    divident, next_expression = get_next_divident(expression)

    dividents.append(divident)
    expressions.append(next_expression)

    filtered_next_expression = list(filter(lambda x: x != 0,next_expression))
    factor(filtered_next_expression)

factor(numbers)