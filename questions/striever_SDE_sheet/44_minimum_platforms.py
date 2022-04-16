class Solution:
    def minimumPlatform(self, n, arr, dep):
        arr.sort()
        dep.sort()

        i, j = 1, 0
        res = 1
        platformsNeeded = 1
        while i < n and j < n:
            if arr[i] > dep[j]:
                platformsNeeded -= 1
                j += 1
            else:
                platformsNeeded += 1
                i += 1

            res = max(platformsNeeded, res)

        return res
