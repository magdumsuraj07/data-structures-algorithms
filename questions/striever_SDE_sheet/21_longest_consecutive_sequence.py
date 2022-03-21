class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}

        # Push all numbers in hashmap
        for num in nums:
            hashMap[num] = False

        maxCount = 0
        for num in nums:
            if (num - 1) not in hashMap:
                currCount = 1
                currNum = num
                while (currNum + 1) in hashMap:
                    currCount += 1
                    currNum += 1

                maxCount = max(maxCount, currCount)

        return maxCount
