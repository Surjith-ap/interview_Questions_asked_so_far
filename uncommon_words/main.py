def uncommonWords(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    
    set1 = set(words1)
    set2 = set(words2)

    uncommon = list(set1.symmetric_difference(set2))
    
    return uncommon  

s1 = "copper coffee pot"
s2 = "hot coffee pot"
print(uncommonWords(s1, s2))