class Solution:
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        d = {}
        currSum = 0
        for num in arr:
            d[currSum] = None
            currSum += num
            if (currSum in d):
                return True
        return False
