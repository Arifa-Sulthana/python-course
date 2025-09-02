def roman_to_integer(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(s)):
        current_value = values[s[i]]
        if i < len(s) - 1:
            next_value = values[s[i + 1]]
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value
    return total

print(roman_to_integer("III"))    # 3
print(roman_to_integer("IV"))     # 4
print(roman_to_integer("MCMXCIV"))  # 1994