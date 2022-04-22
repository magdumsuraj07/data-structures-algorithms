class Solution:
    def getPermutation(self, n, k):
        fact = 1
        nums = []

        # Calculate factorial(n-1) and generate nums array
        for i in range(1, n):
            fact *= i
            nums.append(i)

        # Append last num in nums array
        nums.append(n)

        # Using for 0-based indexing
        k -= 1
        ans = ""
        while True:
            ans += str(nums[k // fact])
            nums.remove(nums[k // fact])
            if len(nums) == 0:
                break

            k = k % fact
            fact //= len(nums)

        return ans
