def print_shortest_substrings(s, x):
    shortest_length = float('inf')
    shortest_substrings = []

    for i in range(len(s)):
        for j in range(i + x - 1, len(s)):
            if s[i] == s[j] and j - i + 1 >= x:
                substring = s[i:j+1]
                if len(substring) < shortest_length:
                    shortest_length = len(substring)
                    shortest_substrings = [substring]
                elif len(substring) == shortest_length:
                    shortest_substrings.append(substring)

    if shortest_substrings:
        for substring in shortest_substrings:
            print(substring)
    else:
        print("not-found")

# Example usage
s = "abccdbacca"
x = 3
print("x =", x)
print_shortest_substrings(s, x)

x = 4
print("\nx =", x)
print_shortest_substrings(s, x)

x = 5
print("\nx =", x)
print_shortest_substrings(s, x)

x = 6
print("\nx =", x)
print_shortest_substrings(s, x)

x = 7
print("\nx =", x)
print_shortest_substrings(s, x)

x = 8
print("\nx =", x)
print_shortest_substrings(s, x)
