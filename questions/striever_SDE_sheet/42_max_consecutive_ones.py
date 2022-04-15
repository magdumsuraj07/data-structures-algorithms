class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currCount = 0
        for num in nums:
            if num == 0:
                currCount = 0
            else:
                currCount += 1
                maxCount = max(maxCount, currCount)
        return maxCount
