class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Moore's voting algorithm
        num1 = -1
        num2 = -1
        count1 = 0
        count2 = 0
        for ele in nums:
            if ele == num1:
                count1 += 1
            elif ele == num2:
                count2 += 1
            elif count1 == 0:
                num1 = ele
                count1 = 1
            elif count2 == 0:
                num2 = ele
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        ans = []
        count1 = 0
        count2 = 0
        for ele in nums:
            if ele == num1:
                count1 += 1
            elif ele == num2:
                count2 += 1

        # Check if count is more than n//3
        n = len(nums)
        if count1 > n // 3:
            ans.append(num1)
        if count2 > n // 3:
            ans.append(num2)

        return ans
