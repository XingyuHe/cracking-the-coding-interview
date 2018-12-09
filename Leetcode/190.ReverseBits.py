def reverseBits(n):


    ans = 0

    temp = n
    number_digit = 0
    while temp > 0:

        temp, digit = divmod(temp, 2)
        ans *= 2
        ans += digit
        number_digit += 1

    return ans * 2 ** (32 - number_digit)

print(reverseBits(5))
print(reverseBits(43261596))
