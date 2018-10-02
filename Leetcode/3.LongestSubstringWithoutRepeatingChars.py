import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = r = 0
        seen_dict = {}
        local_distance = global_distance = 0

        while r < len(s) and l < len(s):

            if s[r] not in seen_dict:
                seen_dict[s[r]] = r
            else:
                l = max(seen_dict[s[r]] + 1, l)
                seen_dict[s[r]] = r
            local_distance = r - l + 1
            if global_distance < local_distance:
                global_distance = local_distance

            r += 1

        return global_distance

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        gm = 0
        lm = 0
        index_dict = {}
        stack = collections.deque()

        for i in range(len(s)):
            char = s[i]
            stack.append(i)

            if char in index_dict:
                last_index = index_dict[char]
                index_dict[char] = i
                while stack[0] <= last_index:
                    stack.popleft()
                lm = i - stack[0] + 1
            else:
                lm += 1
                index_dict[char] = i

            if gm < lm:
                gm = lm

        return gm