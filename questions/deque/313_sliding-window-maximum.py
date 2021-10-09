# Question link below :
# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

from collections import deque


def maxSlidingWindow(arr, n, k):
    output = []
    q = deque()  # Used for storing index

    # Process first k elements (first window)
    for i in range(k):
        # Remove all elements smaller than currently being added element
        while q and arr[i] >= arr[q[-1]]:
            q.pop()

        q.append(i)
    output.append(arr[q[0]])

    # Process rest of elements i.e. arr[k] to arr[n-1]
    for i in range(k, n):
        # Remove elements which are out of window
        while q and (q[0] <= i-k):
            q.popleft()

        # Remove all elements smaller than currently being added element
        while q and arr[i] >= arr[q[-1]]:
            q.pop()

        q.append(i)

        output.append(arr[q[0]])

    return output


if __name__ == '__main__':
    arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    n = len(arr)
    k = 4
    print(maxSlidingWindow(arr, n, k))
