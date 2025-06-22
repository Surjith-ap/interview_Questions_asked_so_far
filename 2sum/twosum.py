# This question is asked by Google. Given an array of integers, return whether or not two numbers sum to a given target, k.
# Note: you may not sum a number with itself.

# Ex: Given the following...

# [1, 3, 8, 2], k = 10, return true (8 + 2)
# [3, 9, 13, 7], k = 8, return false
# [4, 2, 6, 5, 2], k = 4, return true (2 + 2)

def twosum(nums, target):
    return any(nums[i] + nums[j] == target 
               for i in range(len(nums)) 
               for j in range(i + 1, len(nums)))

# Test cases
list1 = [1, 3, 8, 2]
list2 = [3, 9, 13, 7]
list3 = [4, 2, 6, 5, 2]
t1 = 10
t2 = 8
t3 = 4

# Check all test cases
result1 = twosum(list1, t1)
result2 = twosum(list2, t2)
result3 = twosum(list3, t3)

# Print results
print(f"[1, 3, 8, 2], k = 10: {result1}")
print(f"[3, 9, 13, 7], k = 8: {result2}")
print(f"[4, 2, 6, 5, 2], k = 4: {result3}")