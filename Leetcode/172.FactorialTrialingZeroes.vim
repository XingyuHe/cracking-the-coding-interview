def trailingZeroes(n):

    n_10, digit = divmod(n, 10)
    n_5 = n_10 + digit // 5 	
    print n_10, n_5
    return n_10 + n_5
    
print trailingZeroes(30)
import math
print math.factorial(30)
