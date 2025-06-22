# Given a string, return the index of its first unique character. If a unique character does not exist, return -1.

# Ex: Given the following strings...

# "abcabd", return 2
# "thedailybyte", return 1
# "developer", return 0

def uniq():
    test_String = "aa"
    char_count = {}

    for charr in test_String:
        char_count[charr] = char_count.get(charr, 0) + 1
    for index, char in enumerate(test_String):
        if char_count[char] == 1:
            return index
    return -1
result = uniq()
print(result)
