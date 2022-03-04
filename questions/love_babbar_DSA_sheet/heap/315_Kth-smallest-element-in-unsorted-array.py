import heapq


def kthSmallest(arr, left, right, k):
    heapq.heapify(arr)
    for i in range(k):
        ele = heapq.heappop(arr)
    return ele


if __name__ == '__main__':
    n = 5
    k = 4
    arr = [7, 10, 4, 20, 15]
    print(kthSmallest(arr, 0, n-1, k))
