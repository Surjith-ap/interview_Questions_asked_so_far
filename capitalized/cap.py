# This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

# Ex: Given the following strings...

# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true

def caps(test_string):
    if test_string.isupper():
        return True
    elif test_string.islower():
        return True
    elif test_string[0].isupper() and test_string[1:].islower():
        return True
    else:
        return False
test_cases = ["USA", "Calvin", "compUter", "coding"]
for test_string in test_cases:
    result = caps(test_string)
    print(f'"{test_string}" => {result}')