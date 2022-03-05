class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        while (i >= 0):
            if (nums[i] < nums[i+1]):
                break
            i -= 1
        if (i < 0):
            nums.reverse()
        else:
            j = n-1
            while (j > i):
                if (nums[j] > nums[i]):
                    break
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = reversed(nums[i+1:])
