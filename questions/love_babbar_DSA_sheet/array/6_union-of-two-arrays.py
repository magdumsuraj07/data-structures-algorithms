class Solution:
    def doUnion(self, a, n, b, m):
        return len(set(a).union(set(b)))


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3]
    sol = Solution()
    unionCount = sol.doUnion(a, len(a), b, len(b))
    print(unionCount)
