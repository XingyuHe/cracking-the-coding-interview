def merge(nums1, m, nums2, n):
    i = j = 0
    while j < n and i < m:
        ele1 = nums1[i]
        ele2 = nums2[j]

        if ele1 >= ele2:

            nums1[i + 1: m + 1] = nums1[i: m]
            nums1[i] = nums2[j]
            m += 1

            j += 1

        else:
            i += 1

    nums1[m: m + n] = nums2[j:n]
    return nums1


print merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print merge([1, 2, 3, 0, 0, 0], 3, [1,2], 2)
print merge([1], 0, [9, 2, 3], 1)
print merge([1], 1, [], 0 )

A = [4,0,0,0,0,0]
m = 1
B = [1,2,3,5,6]
n = 5
print merge(A, m , B, n)
