def containsDuplicate(nums):

    from collections import Counter
    fq = Counter(nums)
    return fq.most_common(1)[0][1] > 1

def faster(nums):

    return len(set(nums)) != len(nums)

def evenFaster(nums):

    fq = set([])
    for n in nums:
        if n in fq:
            return False

        fq.add(n)

    return True

print containsDuplicate([1, 2, 3, 4, 5])
print containsDuplicate([1, 1, 2, 3, 4])
