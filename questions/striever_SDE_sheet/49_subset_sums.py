class Solution:
    def subsetSumsHelper(self, arr, N, index, currSum, allSums):
        if index == N:
            allSums.append(currSum)
            return

        # Pick current number
        self.subsetSumsHelper(arr, N, index + 1, currSum + arr[index], allSums)

        # Skip current number
        self.subsetSumsHelper(arr, N, index + 1, currSum, allSums)

    def subsetSums(self, arr, N):
        allSums, index, currSum = [], 0, 0
        self.subsetSumsHelper(arr, N, index, currSum, allSums)
        return allSums
