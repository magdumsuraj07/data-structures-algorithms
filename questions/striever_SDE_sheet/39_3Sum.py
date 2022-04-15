from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                reqSum = 0 - nums[i]
                lo = i + 1
                hi = n - 1
                while lo < hi:
                    if (nums[lo] + nums[hi]) < reqSum:
                        lo += 1
                    elif (nums[lo] + nums[hi]) > reqSum:
                        hi -= 1
                    else:
                        res.append([nums[i], nums[lo], nums[hi]])
                        # Skip duplicates
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        # Skip duplicates
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1

                        lo += 1
                        hi -= 1

        return res
