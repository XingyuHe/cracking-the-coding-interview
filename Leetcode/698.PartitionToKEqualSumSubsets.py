def canPartitionKSubsets(nums, k):

    n = len(nums)
    target_value = sum(nums) / k

    if target_value % 1 != 0 :
        return False

    nums.sort()
    while nums:
        max_ = nums.pop()
        temp_target = target_value - max_
        if max_ == target_value:
            pass
        elif max_ > target_value:
            return False
        else:
            while temp_target > nums[-1]:

                min_ = nums.leftpop()
                temp_target = temp_target - min_

                if min_ > temp_target:
                    return False
    return True



canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)

