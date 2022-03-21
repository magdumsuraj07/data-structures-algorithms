class Solution:
    def maxLen(self, n, arr):
        maxLength = 0
        currSum = 0
        hashMap = {}
        for i in range(n):
            currSum += arr[i]
            if currSum == 0:
                maxLength = i + 1
            elif currSum in hashMap:
                maxLength = max(maxLength, i - hashMap[currSum])
            else:
                hashMap[currSum] = i

        return maxLength
