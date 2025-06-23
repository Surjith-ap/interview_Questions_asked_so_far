def intersec(nums1, nums2):
    intersected = []

    for num in nums1:
        if num in nums2 and num not in intersected:
            intersected.append(num)
    return intersected

nums1 = [2, 4, 6, 8]
nums2 = [1, 3, 5, 7]
result = intersec(nums1, nums2)
print(result)