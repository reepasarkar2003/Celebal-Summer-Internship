# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

# Read the input string
s = input().strip()

# Use groupby to group consecutive characters
grouped = [(len(list(group)), int(char)) for char, group in groupby(s)]

# Print the result as specified in the output format
print(" ".join(str(item) for item in grouped))