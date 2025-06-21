charr = "cfghdddxfsss"
char_count = {}

for char in charr:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
result = ''.join(f"{key}{value}" if value > 1 else key for key, value in char_count.items())
print(char_count)
print(result)