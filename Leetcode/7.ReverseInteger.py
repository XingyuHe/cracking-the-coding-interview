def reverse(x):

    def helper(s):

        if not s:
            return s

        return s[-1] + helper(s[:-1])

    sn = str(x)
    ans = helper(sn[1:])
    if sn[0] != "-":
        ans = ans + sn[0]
    else:
        ans = sn[0] + ans

    ans = int(ans)

    if ans >= -2 ** 31 and ans < 2 ** 31:
        return ans

    return 0

def Faster(x):

    ans = 0
    temp = x if x > 0 else -x

    while temp > 0:

        temp, digit = divmod(temp, 10)

        ans *= 10
        ans += digit

    ans = ans if x > 0 else -ans

    if ans >= -2 ** 31 and ans < 2 ** 31:
        return ans

    return 0




print reverse(-123456)
print reverse(1534236469)
print Faster(-123456)
print Faster(1534236469)
print 2 ** 31 - 1
print -2** 31
