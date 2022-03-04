from collections import deque


class Solution:
    def sorted(self, S):
        if (S):
            temp = S.pop()
            self.sorted(S)
            self.sortedInsert(S, temp)

    def sortedInsert(self, S, ele):
        if (not S or ele >= S[-1]):
            S.append(ele)
        else:
            temp = S.pop()
            self.sortedInsert(S, ele)
            S.append(temp)


if __name__ == '__main__':
    S = deque()
    S.append(11)
    S.append(2)
    S.append(32)
    S.append(3)
    S.append(41)
    print(list(S))
    sol = Solution()
    sol.sorted(S)
    print(list(S))
