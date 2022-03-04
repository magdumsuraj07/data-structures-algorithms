from sys import maxsize as MAX_INT

def minJumps(arr, n, si, dp):
    if (si == n-1):
        return 0
    if (si > n-1):
        return MAX_INT
    maxReach = arr[si]
    if (maxReach == 0):
        return -1
    
    minijumps = MAX_INT
    for i in range(1, maxReach+1):
        if (si+i < n):
            if (dp[si+i] == MAX_INT):
                jumps = minJumps(arr, n, si+i, dp)
                dp[si+i] = jumps
            else:
                jumps = dp[si+i]
            if (jumps < minijumps):
                minijumps = jumps
    if (minijumps == -1):
        return -1
    return 1 + minijumps


def minJumpsIterative(arr, n):
    dp = [MAX_INT for i in range(n)]
    dp[n-1] = 0
    for i in range(n-2, -1, -1):
        maxReach = arr[i]
        if (maxReach == 0):
            continue
        elif (maxReach >= n-i-1):
            dp[i] = 1
        else:
            miniJumps = min(dp[i+1:i+maxReach+1], default=MAX_INT)
            if (miniJumps == MAX_INT):
                dp[i] = MAX_INT
            else:
                dp[i] = 1 + miniJumps
    if (dp[0] == MAX_INT):
        return -1
    return dp[0]





# arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = [1, 0, 3, 2, 6, 7]
n = len(arr)
dp = [MAX_INT for i in range(n)]
dp[n-1] = 0
print(minJumps(arr, n, 0, dp))