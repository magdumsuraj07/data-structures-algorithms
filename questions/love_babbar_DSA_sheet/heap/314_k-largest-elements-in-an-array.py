import heapq


def kLargest(arr, n, k):
    heapq.heapify(arr)
    return heapq.nlargest(k, arr)


if __name__ == '__main__':
    n = 5
    k = 2
    arr = [12, 5, 787, 1, 23]
    print(kLargest(arr, n, k))