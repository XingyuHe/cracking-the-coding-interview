def firstUniqChar(s):

    # Intuitively
    from collections import Counter
    fq = Counter(list(s))

    for i in range(len(s)):

        if fq[s[i]] == 1:
            return i

    return -1

def faster(s):
    # Using string manipulation

    ans = len(s)

    for char in "abcdefghijklmnopqrstuvwxyz":

        find = s.find(char)
        rfind = s.rfind(char)

        #check if the character is a duplication
        if find != -1:
            if find == s.rfind(char):
                ans = min(ans, s.find(char))

    if ans == len(s):
        return -1
    return ans

print faster("leetcode")
