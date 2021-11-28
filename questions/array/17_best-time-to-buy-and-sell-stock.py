class Solution:
    def maxProfit(self, prices):
        minSoFar = prices[0]
        maxProfit = 0
        for price in prices:
            if (price < minSoFar):
                minSoFar = price
            currProfit = price - minSoFar
            if (currProfit > maxProfit):
                maxProfit = currProfit
        return maxProfit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
