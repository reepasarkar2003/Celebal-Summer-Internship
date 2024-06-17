def average(array):
    # Convert the array to a set to remove duplicates
    distinct_heights = set(array)
    
    # Calculate the sum of the distinct heights
    total_height = sum(distinct_heights)
    
    # Calculate the number of distinct heights
    num_distinct_heights = len(distinct_heights)
    
    # Calculate the average height
    average_height = total_height / num_distinct_heights
    
    # Return the average height rounded to 3 decimal places
    return round(average_height, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
