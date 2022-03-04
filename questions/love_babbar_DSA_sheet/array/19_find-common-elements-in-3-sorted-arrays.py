class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        i = j = k = 0
        res = []
        while (i < n1 and j < n2 and k < n3):
            if (A[i] == B[j] and B[j] == C[k]):
                # Check for duplicate elemtns
                if (A[i] not in res):
                    res.append(A[i])
                i += 1
                j += 1
                k += 1
            else:
                if (A[i] <= B[j] and A[i] <= C[k]):
                    i += 1
                elif (B[j] <= A[i] and B[j] <= C[k]):
                    j += 1
                else:
                    k += 1
        return res


if __name__ == '__main__':
    A = [1, 5, 10, 20, 40, 80]
    B = [6, 7, 20, 80, 100]
    C = [3, 4, 15, 20, 30, 70, 80, 120]
    print(Solution().commonElements(A, B, C, len(A), len(B), len(C)))
