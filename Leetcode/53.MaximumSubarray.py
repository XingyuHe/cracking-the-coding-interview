class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        global_max = local_max = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]
            local_max = max(local_max + num, num)

            if global_max < local_max:
                global_max = local_max

        return global_max
