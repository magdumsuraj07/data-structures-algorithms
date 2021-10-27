import heapq


def kthLargestSumContiguousSubarray(arr, k, n):
    # Find all possible sums
    sumArray = []
    for i in range(n):
        currSum = arr[i]
        sumArray.append(currSum)
        for j in range(i+1, n):
            currSum += arr[j]
            sumArray.append(currSum)

    # Find k-th largest sum using min heap of size k
    heap = []
    for i in range(len(sumArray)):
        if (i < k):
            heapq.heappush(heap, sumArray[i])
        else:
            if (heap[0] < sumArray[i]):
                heapq.heapreplace(heap, sumArray[i])

    return heapq.heappop(heap)


if __name__ == '__main__':
    arr = [10, -10, 20, -40]
    k = 6
    n = len(arr)
    print(kthLargestSumContiguousSubarray(arr, k, n))
