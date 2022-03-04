from collections import deque


class Solution:
    def celebrity(self, M, n):
        stack = deque()

        # Push all persons in stack
        for i in range(n):
            stack.append(i)
        while (len(stack) > 1):
            personA = stack.pop()
            personB = stack.pop()
            if (M[personA][personB] == 1):
                # PersonA knows personB; hence personA cann't be celebrity
                stack.append(personB)
            else:
                # PersonA doesn't know personB;
                # hence personB cann't be celebrity
                stack.append(personA)

        possibleCeleb = stack[-1]
        for i in range(n):
            if (i == possibleCeleb):
                continue
            if (M[i][possibleCeleb] != 1):
                return -1
            if (M[possibleCeleb][i] == 1):
                return -1
        return possibleCeleb


if __name__ == '__main__':
    M = [[0, 1, 0],
         [0, 0, 0],
         [0, 1, 0]]
    n = 3
    sol = Solution()
    print(sol.celebrity(M, n))
