def maxProfit(self, prices):
    small=prices[0]
    large=0
    for i in prices:
        if i<small:
            small=i
        else:
            large=max(large,i-small)
    return large