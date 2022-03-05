class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        maxProfit = 0
        for price in prices:
            if (price < minSoFar):
                minSoFar = price
            currProfit = price - minSoFar
            if (currProfit > maxProfit):
                maxProfit = currProfit
        return maxProfit
