import re

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    # Number of test cases
    T = int(data[0])
    
    # Process each test case
    for i in range(1, T + 1):
        regex_string = data[i]
        
        try:
            re.compile(regex_string)
            print("True")
        except re.error:
            print("False")

if __name__ == "__main__":
    main()
