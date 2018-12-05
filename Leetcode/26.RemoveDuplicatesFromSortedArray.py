def removeDuplicates(nums):
    current =  0
    runner = current + 1

    while runner < len(nums):
        if nums[current] == nums[runner]:
            while runner < len(nums) and nums[runner] == nums[current]:
                nums.pop(runner)
        else:
            runner += 1
            current += 1

    print nums


removeDuplicates([1, 2, 3,4,4, 5])
removeDuplicates([])
removeDuplicates([1,1])
