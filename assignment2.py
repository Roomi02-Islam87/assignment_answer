def code_string(s):
    s1 = ""
    s2 = set()

    for i in range(len(s)):
        char = s[i]
        ascii_value = ord(char)

        if ascii_value % 2 == 0:
            if i + 1 < len(s) and s[i + 1] not in s2:
                next_ch = chr((ascii_value % 7) + ord(s[i + 1]))
                if ord(next_ch) > 127:
                    next_ch = chr(83)
                s1 += char + next_ch
                s2.add(s[i + 1])
            else:
                s1 += char
        else:
            if i - 1 >= 0 and s[i - 1] not in s2:
                prev_ch = chr(ord(s[i - 1]) - (ascii_value % 5))
                if ord(prev_ch) < 0:
                    prev_ch = chr(83)
                s1 += prev_ch + char
                s2.add(s[i - 1])
            else:
                s1 += char

    return s1

# Example usage
s = "sHQen}"
s1 = code_string(s)
print(s1)
