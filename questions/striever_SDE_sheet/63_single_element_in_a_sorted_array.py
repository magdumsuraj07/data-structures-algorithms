class Solution:
    def singleNonDuplicate(self, nums):
        low, high = 0, len(nums) - 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]
