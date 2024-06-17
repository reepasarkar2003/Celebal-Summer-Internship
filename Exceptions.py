def main():
    import sys
    input = sys.stdin.read
    
    # Read input
    data = input().splitlines()
    
    # Number of test cases
    T = int(data[0])
    
    # Process each test case
    for i in range(1, T + 1):
        x, y = data[i].split()
        
        try:
            result = int(x) // int(y)
            print(result)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)

if __name__ == "__main__":
    main()
