def LongestCommonPrefix(strs):

    def common_head(ans, s):
        new_ans = ""
        for i in range(min(len(ans), len(s))):
            if ans[i] != s[i]:
                return new_ans

            new_ans += ans[i]

        return new_ans

    if not strs:
        return 0
    ans = strs[0]

    for s in strs:
        print ans, s
        ans = common_head(ans, s)

    return len(ans)


def recursive(strs):

    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    s = strs[0]
    ans =  recursive(strs[1:])
    for i in range(len(ans)):
        if i >= len(s):
            return ans[:i]
        if ans[i] != s[i]:
            return ans[:i]
    return ans

strs = ["abcdefg", "abcdehh"]
print LongestCommonPrefix(strs)
print recursive(strs)
print recursive(["","b"])
print recursive([])
print recursive(["aaa","aa", "aaa"])

