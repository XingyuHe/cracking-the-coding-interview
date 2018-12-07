def titleToNumber(s):

    ans = 0

    for i in range(len(s)):

        base = 26 ** (len(s) - i - 1)
        digit = ord(s[i]) - 64

        ans += digit * base

    return ans

def fastertitleToNumber(s):

    ans = 0

    for i in range(len(s)):
        ans += 26 ** (len(s) - i - 1) * (ord(s[i]) - 64)

    return ans



print titleToNumber("AA")

print fastertitleToNumber("AA")
