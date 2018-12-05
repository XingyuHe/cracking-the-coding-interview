def merge(nums1, m, nums2, n):

    i = j = 0
    count = 0
    while i < m + n and j < n :
        if nums1[i] < nums2[j] and nums1[i] != 0:
            i += 1
            count += 1

        else:
            for k in range()
            j += 1
            i += 1
            count -= 1

    for i in range(m + n, len(nums1)):
        nums1.pop(i)


print merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print merge([1], 0, [9, 2, 3], 1)

