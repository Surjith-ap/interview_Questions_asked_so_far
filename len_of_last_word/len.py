def lengthOfLastWord():
    test_string = "luffy is still joyboy".split()
    length = len(test_string)
    result = len(test_string[length-1])
    print(result)
lengthOfLastWord()