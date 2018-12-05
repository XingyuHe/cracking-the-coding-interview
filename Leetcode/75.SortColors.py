def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    freq = {}
    for n in nums:
        freq[n] = 1 + freq.get(freq[n], 0)

    return freq[0] * [0] + freq[1] * [1] + freq[2] * [2]

print sortColors([0, 1,2,1,0])
