def longestConsecutiveSequence(nums):

    nums_set = {}
    gm = 0

    for n in nums:
        nums_set[n] = nums_set.get(n, 0) + 1

    for num in nums_set.keys():
#        print(num)
        if num in nums_set:
            if num - 1 not in nums_set:
                streak = nums_set[num]
                while num + 1 in nums_set:
                    streak += nums_set[num + 1]
                    del nums_set[num  + 1]
                    num += 1
                gm = max(streak, gm)
    return gm


print longestConsecutiveSequence([100, 1, 90, 2, 3, 4])
print longestConsecutiveSequence([100, 4, 200, 1, 3, 2])
