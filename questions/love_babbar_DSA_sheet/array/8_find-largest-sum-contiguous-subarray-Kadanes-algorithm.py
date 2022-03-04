from sys import maxsize as MAX_INT

class Solution:
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        maxSum = -1 * MAX_INT
        currSum = 0
        for num in arr:
            currSum += num
            if (currSum > maxSum):
                maxSum = currSum
            if (currSum < 0):
                currSum = 0
        return maxSum
 