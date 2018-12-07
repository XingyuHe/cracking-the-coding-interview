def isHappy(n):

    r = set([])
    h = set([1, 82, 68, 100])
    while n not in r:
        r.add(n)
        n = sum(map(lambda x: int(x) ** 2, str(n))) 
        if n in h:
            return True
    print r
    return False

def Faster(n):

    r = set([])
    while True:
        
        if 1 in r:
            return True
        if n in r:
            return False

        r.add(n)
        temp = 0
        
        while n > 0:
            divisor, rem = divmod(n, 10)
            temp += rem ** 2
            n = divisor
        n = temp
        
        
print Faster(10)

print isHappy(7)
