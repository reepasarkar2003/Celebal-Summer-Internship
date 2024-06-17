from collections import Counter

def main():
    # Read the number of shoes
    num_shoes = int(input())
    
    # Read the list of shoe sizes and store them in a Counter
    shoe_sizes = list(map(int, input().split()))
    inventory = Counter(shoe_sizes)
    
    # Read the number of customers
    num_customers = int(input())
    
    total_earnings = 0
    
    # Process each customer
    for _ in range(num_customers):
        size, price = map(int, input().split())
        
        # Check if the desired shoe size is available
        if inventory[size] > 0:
            total_earnings += price
            inventory[size] -= 1
    
    # Print the total earnings
    print(total_earnings)

if __name__ == "__main__":
    main()
