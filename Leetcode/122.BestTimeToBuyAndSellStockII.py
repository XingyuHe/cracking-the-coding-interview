def BFmaxProfit(prices):
    prev = prices[0]
    ans = 0
    for i in range(1, len(prices)):
        curr = prices[i]

        prices[i] = curr - prev

        prev = curr

    for i in range(1, len(prices)):

        if prices[i] > 0:
            ans += prices[i]

    return ans

# Yea, the author should have add the restriction that you cannot buy and sell at the same day
print BFmaxProfit([1, 2, 3, 4, 5])
print BFmaxProfit([7,6,4,3,1])
