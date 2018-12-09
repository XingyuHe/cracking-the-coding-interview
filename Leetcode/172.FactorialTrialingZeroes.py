def trailingZeroes(n):
    from math import log 
    b_n = int(log(n) / log(5))
    ans = 0
    for i in range(1, b_n + 1):
        ans += n // (5 ** i)

    return ans


def Faster(n):

    if n == 0:
        return 0
    return n // 5 + Faster(n // 5)
        
    
print trailingZeroes(30)
import math
print math.factorial(30)
print Faster(30)
