# ✅ Basic Syntax

# [expression for item in iterable if condition]

squares = [x*x for x in range(5)]
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

words = ['python', 'is', 'awesome']
lengths = [len(word) for word in words]
print(lengths)  # [6, 2, 7]

pairs = [(x, y) for x in range(2) for y in range(3)]
print(pairs)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

nums = [int(x) for x in input().split()]