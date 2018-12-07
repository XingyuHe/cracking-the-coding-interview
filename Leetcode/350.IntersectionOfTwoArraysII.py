def intersect(nums1, nums2):

    # brute force solution
    ans = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                print i, j
                i_, j_ = i, j
                while i_ < len(nums1) and j_ < len(nums2) and nums1[i_] == nums2[j_]:

                    ans.append(nums1[i_])
                    i_ += 1
                    j_ += 1
                return ans

def intersect_dict(nums1, nums2):
    import collections

    C = collections.Counter
    c1 = C(nums1)
    c2 = C(nums2)

    print c1 , c2
    print c1 & c2

print intersect([1, 2, 2, 1], [2, 2])
print intersect_dict([1, 2, 2, 1], [2, 2])
