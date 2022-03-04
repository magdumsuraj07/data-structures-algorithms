# Question Link :
# https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes/0

import heapq


def minCost(arr, n):
    heapq.heapify(arr)
    total = 0

    for i in range(n-1):

        # Get 2 smallest elements from heap and pop
        firstSmallEle = heapq.heappop(arr)
        secondSmallEle = heapq.heappop(arr)

        additionTwoSamllestElements = firstSmallEle + secondSmallEle
        total += additionTwoSamllestElements

        heapq.heappush(arr, additionTwoSamllestElements)

    return total


if __name__ == '__main__':
    n = 5
    arr = [4, 2, 7, 6, 9]
    print(minCost(arr, n))
