class Solution(object):

    def threeSumClosest(self, nums, target):

        nums.sort()
        min_c = nums[0] + nums[1] + nums[-1]

        print nums

        for i in range(len(nums) - 2):

            r = len(nums) - 1
            l = i + 1

            while l < r:

                curr = nums[l] + nums[r] + nums[i]

                if curr == target:
                    return curr
                elif abs(curr - target) < abs(min_c - target):
                    min_c = curr

                if curr > target:
                    r -= 1
                else:
                    l += 1

        return min_c


    def twoSum(self, nums, target):

        set_ = {}

        for i in range(len(nums)):

            if target - nums[i] in set_:
                return i, set_[target - nums[i]]

            else:
                set_[nums[i]] = i

        return
        # result = []
        # nums.sort()
        # l = 0
        # r = len(nums) - 1
        #
        # while l < r:
        #
        #     diff =  target - nums[l] - nums[r]
        #
        #     if diff < 0:
        #
        #         l += 1
        #
        #     elif diff > 0:
        #
        #         r -= 1
        #
        #     else:
        #         result.extend([nums[l], nums[r]])
        #
        #         while l < r and nums[l] == nums[l + 1]:
        #             l += 1
        #         while l < r and nums[r] == nums[r - 1]:
        #             r -= 1




