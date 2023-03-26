#!/usr/bin/python3

from math import gcd
import sys

numbers = [int(x) for x in sys.argv[1:]]

print(gcd(*numbers))