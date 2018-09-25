def fibonacci_multiply(a, b):

    fib = []
    fib.append(1)
    fib.append(1)

    ma = []
    ma.append(a)
    ma.append(a)

    while fib[-1] < b:
        fib.append(fib[-1] + fib[-2])
        ma.append(ma[-1] + ma[-2])

    summ = 0
    g = b

    print fib

    while g > 0:

        # print fib, ma, summ, g
        if g >= fib[-1]:
            g -= fib[-1]
            summ += ma[-1]

        fib.pop()
        ma.pop()

    return summ

def recursive_multiply1(a, b):


    smaller, bigger = (a, b) if a < b else (b, a)

    return recursive_multiply1_helper(smaller, bigger)


def recursive_multiply1_helper(smaller, bigger):

    if smaller == 1:
        return bigger
    if smaller == 0:
        return 0

    s = smaller // 2
    first_half = recursive_multiply1_helper(s, bigger)
    second_half = first_half
    if smaller & 1 == 1:
        second_half = recursive_multiply1_helper(smaller - s, bigger)

    return first_half + second_half

def recursive_multiply2(a, b):

    smaller, bigger = (a, b) if a < b else (b, a)

    return recursive_multiply2_helper(smaller, bigger)

cache = {}
def recursive_multiply2_helper(smaller, bigger):


    if smaller == 1:
        return bigger
    if smaller == 0:
        return 0
    if smaller in cache:
        return cache[smaller]

    first_half = 0
    second_half = 0
    s = smaller // 2
    first_half = recursive_multiply2_helper(s, bigger)

    second_half = first_half

    if smaller & 1 == 1:
        second_half = recursive_multiply2_helper(smaller - s, bigger)

    cache[smaller] = first_half + second_half
    return cache[smaller]



def recursive_multiply3(a, b):

    smaller, bigger = (a, b) if a < b else (b, a)

    return recursive_multiply3_helper(smaller, bigger)

cache2 = {}
def recursive_multiply3_helper(smaller, bigger):


    if smaller == 1:
        return bigger
    if smaller == 0:
        return 0
    if smaller in cache2:
        return cache2[smaller]

    first_half = 0
    second_half = 0
    s = smaller // 2
    first_half = recursive_multiply3_helper(s, bigger)

    second_half = first_half + bigger if smaller & 1 == 1 else first_half

    cache2[smaller] = first_half + second_half
    return cache2[smaller]



print fibonacci_multiply(1 >> 10, 999999999)
print recursive_multiply1(10, 5)
print recursive_multiply2(10, 9999090909)
print recursive_multiply3(10, 5)