# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

def calculate_probability(n, letters, k):
    indices = list(range(n))
    total_combinations = list(itertools.combinations(indices, k))
    valid_combinations = 0
    
    for combination in total_combinations:
        if any(letters[i] == 'a' for i in combination):
            valid_combinations += 1
            
    probability = valid_combinations / len(total_combinations)
    return probability

# Reading input
n = int(input().strip())
letters = input().strip().split()
k = int(input().strip())

# Calculating probability
result = calculate_probability(n, letters, k)

# Printing the result formatted to 4 decimal places
print(f"{result:.4f}")