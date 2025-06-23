def intersec(nums1, nums2):
    intersected = []

    for num in nums1:
        if num in nums2 and num not in intersected:
            intersected.append(num)
    return intersected

nums1 = [2, 4, 4, 2]
nums2 = [2, 4]
result = intersec(nums1, nums2)
print(result)