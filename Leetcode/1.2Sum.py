class Solution(object):

    def twoSum(self, nums, target):

        set_ = {}

        for i in range(len(nums)):

            if target - nums[i] in set_:
                return i, set_[target - nums[i]]

            else:
                set_[nums[i]] = i

        return



