from collections import OrderedDict


class Solution:
    def checkMirrorTree(self, n, e, A, B):
        hMapA = OrderedDict()
        hMapB = OrderedDict()

        for i in range(0, e*2, 2):
            if (A[i] not in hMapA.keys()):
                hMapA[A[i]] = []
            hMapA[A[i]].append(A[i+1])

            if (B[i] not in hMapB.keys()):
                hMapB[B[i]] = []
            hMapB[B[i]].append(B[i+1])

        for key in hMapA.keys():
            if (hMapA[key] != list(reversed(hMapB[key]))):
                return 0
        return 1


if __name__ == '__main__':
    n = 7
    e = 7
    A = [1, 2, 1, 3, 2, 4, 2, 5, 5, 6, 6, 7, 6, 9]
    B = [1, 3, 1, 2, 2, 5, 2, 4, 5, 6, 6, 9, 6, 7]
    sol = Solution()
    print(sol.checkMirrorTree(n, e, A, B))
