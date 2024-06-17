#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # We need to iterate through each character and capitalize the start of each word
    capitalized = ''
    capitalize_next = True
    
    for char in s:
        if char == ' ':
            capitalized += char
            capitalize_next = True
        elif capitalize_next:
            capitalized += char.upper()
            capitalize_next = False
        else:
            capitalized += char.lower()
    
    return capitalized

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
