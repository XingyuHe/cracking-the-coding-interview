def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = j = 0
    k = len(nums)- 1

    while j <= k:

        if nums[j] == 0:

            nums[j] = nums[i]
            nums[i] = 0
            i += 1
            j += 1

        elif nums[j] == 2:

            nums[j] = nums[k]
            nums[k] = 2
            k -= 1

        else:

            j += 1

    return nums

print sortColors([0, 1,2,1,0])
