class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndexMap = {}
        for i in range(len(nums)):
            toFind = target - nums[i]
            if toFind in numToIndexMap:
                return [numToIndexMap.get(toFind), i]
            numToIndexMap[nums[i]] = i
