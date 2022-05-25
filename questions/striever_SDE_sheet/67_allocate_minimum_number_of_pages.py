def isPossible(limit, nDays, mChapters, times):
    dayCount = 1
    allocation = 0
    for t in times:
        if t > limit:
            return False
        if allocation + t > limit:
            dayCount += 1
            allocation = t
        else:
            allocation += t
    if dayCount > nDays:
        return False
    return True


def ayushGivesNinjatest(n, m, time):
    # Write your code here.
    low, high = min(time), sum(time)
    while low <= high:
        mid = (low + high) // 2
        if isPossible(mid, n, m, time):
            high = mid - 1
        else:
            low = mid + 1
    return low
