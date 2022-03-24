def subarraysXor(arr, x):
    # Write your code here
    # Return an integer
    n = len(arr)
    subarrayCount = 0
    hashMap = {}
    currXOR = 0
    for i in range(n):
        currXOR = currXOR ^ arr[i]
        if currXOR == x:
            subarrayCount += 1
        if (currXOR - x) in hashMap:
            subarrayCount += hashMap[currXOR - x]
        hashMap[currXOR] = hashMap.get(currXOR, 0) + 1

    return subarrayCount
