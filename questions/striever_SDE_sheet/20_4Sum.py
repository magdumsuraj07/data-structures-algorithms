class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                target_2 = target - nums[i] - nums[j]
                left = j + 1
                right = n - 1

                while left < right:
                    if nums[left] + nums[right] < target_2:
                        left += 1
                    elif nums[left] + nums[right] > target_2:
                        right -= 1
                    else:
                        # Found a quad
                        quad = []
                        quad.append(nums[i])
                        quad.append(nums[j])
                        quad.append(nums[left])
                        quad.append(nums[right])
                        res.append(quad)

                        # Skip duplicates for 3rd number
                        while left < right and nums[left] == quad[2]:
                            left += 1

                        # Skip duplicates for 4th number
                        while left < right and nums[right] == quad[3]:
                            right -= 1

                j += 1
                # Skip duplicates for 2nd number
                while j < n and nums[j - 1] == nums[j]:
                    j += 1

            i += 1
            # Skip duplicates for 1st number
            while i < n and nums[i - 1] == nums[i]:
                i += 1

        return res
