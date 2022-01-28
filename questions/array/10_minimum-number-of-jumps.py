from sys import maxsize as MAX_INT
from tracemalloc import start

def minJumpsHelper(arr, n, startIndex, dp):
    if (startIndex >= n-1):
        return 0
    minimumJumps = MAX_INT
    for j in range(arr[startIndex]+1, 0, -1):
        if (startIndex+j < n):
            if (dp[startIndex+j] == -1):
                jumps = minJumpsHelper(arr, n, startIndex+j, dp)
                dp[startIndex+j] = jumps
            else:
                jumps = dp[startIndex+j]
            jumps += 1
            if (jumps < minimumJumps):
                minimumJumps = jumps
    return minimumJumps



arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
dp = [-1 for x in range(n)]
dp[n-1] = 0
minJumpsHelper(arr, n, 0, dp)
print(dp)