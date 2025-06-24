text1 = "copper coffee pot"
text2 = "hot coffee pot"

words1 = set(text1.lower().split())
words2 = set(text2.lower().split())

# Words in text2 but not in text1
uncommon_words = list(words2 - words1)

print(uncommon_words)