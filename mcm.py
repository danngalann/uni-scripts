#!/usr/bin/python3

from math import lcm
import sys

numbers = [int(x) for x in sys.argv[1:]]

print(lcm(*numbers))