class Solution:
    def getPairsCount(self, arr, n, k):
        d = {}
        count = 0
        for num in arr:
            target = k - num
            count += d.get(target, 0)
            d[num] = d.get(num, 0) + 1
        return count