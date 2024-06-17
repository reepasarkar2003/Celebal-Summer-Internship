def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # Slice the substring
        substring = string[i:i + k]
        
        # Use a set to track seen characters
        seen = set()
        unique_substring = ''
        
        for char in substring:
            if char not in seen:
                unique_substring += char
                seen.add(char)
        
        # Print the unique substring
        print(unique_substring)

if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)
