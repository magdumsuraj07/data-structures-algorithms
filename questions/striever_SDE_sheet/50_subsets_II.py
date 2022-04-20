class Solution:
    def subsetsWithDupHelper(self, nums, i, subset, res):
        if i == len(nums):
            res.append(subset[:])
            return

        # Inclue current number
        subset.append(nums[i])
        self.subsetsWithDupHelper(nums, i + 1, subset, res)
        subset.pop()

        # Exclude current number and duplicates if there are any
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.subsetsWithDupHelper(nums, i + 1, subset, res)

    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        self.subsetsWithDupHelper(0, [], res)
        return res
