class Solution:
    def findDuplicate(self, nums):
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for num, count in d.items():
            if count > 1:
                return num