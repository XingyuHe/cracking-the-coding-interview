def countPrimes(n):


    prime_list = []
    for i in range(2, n):

        isPrime = True
        for prime in prime_list:
            if i % prime == 0:
                isPrime = False
                break
        if isPrime:
            prime_list.append(i)

    return len(prime_list)

def Faster(n):

    def SieveOfEratosthenes(n):

        if n < 2:
            return 0
        Prime = [True] * n
        Prime[0] = False
        Prime[1] = False
        # get rid of all number who is a multiple of n
        for i in range(2, int(n ** 0.5) + 1):
            if Prime[i] == True:
                multiple = i ** 2
                Prime[multiple : :i] = [False] * len(Prime[multiple: : i])


        return sum(Prime)

    return(SieveOfEratosthenes(n))
print countPrimes(10)
print Faster(10)
print Faster(10000)
