def missingAndRepeating(arr, n):
    # Write your code here
    freqArr = [0 for i in range(n + 1)]
    for num in arr:
        freqArr[num] += 1

    for i in range(n + 1):
        if freqArr[i] == 0:
            missing = i
        elif freqArr[i] == 2:
            repeated = i

    return missing, repeated
