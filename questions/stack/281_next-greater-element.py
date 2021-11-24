from collections import deque


class Solution:
    def nextGreaterElement(self, arr, n):
        res = deque()
        stack = deque()

        for i in range(n-1, -1, -1):
            curr = arr[i]
            while(stack and stack[-1] <= curr):
                stack.pop()
            if (len(stack) == 0):
                res.appendleft(-1)
            else:
                res.appendleft(stack[-1])
            stack.append(curr)
        return list(res)


if __name__ == '__main__':
    arr = [1, 3, 2, 4]
    print(Solution().nextGreaterElement(arr, len(arr)))
