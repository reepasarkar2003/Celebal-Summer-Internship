def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])  # number of elements in the set
    s = set(map(int, data[1].split()))  # elements of the set
    num_commands = int(data[2])  # number of commands
    
    commands = data[3:3 + num_commands]  # commands list
    
    for command in commands:
        parts = command.split()
        if parts[0] == 'pop':
            if s:
                s.pop()
        elif parts[0] == 'remove':
            x = int(parts[1])
            if x in s:
                s.remove(x)
        elif parts[0] == 'discard':
            x = int(parts[1])
            s.discard(x)
    
    # Calculate and print the sum of the elements in the set
    print(sum(s))

if __name__ == "__main__":
    main()
