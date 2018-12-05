def coinChange(coins, amount):
    if amount == 0:
        return 0
    C = [amount + 1] * (amount + 1)
    C[0] = 0

    coins.sort()
    for coin in coins:
        for target in range(1, len(C)):
            if target - coin >= 0:
                C[target] = min(C[target], C[target - coin] + 1)
    if C[-1] >= amount:
        return -1
    return C[-1]


print coinChange([186,419,83,408], 6249)
print coinChange([1, 3, 4], 6)
print coinChange([2, 3 ,4], 1)
