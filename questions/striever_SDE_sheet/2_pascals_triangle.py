from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        prev = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if (j == 0 or j == i):
                    row.append(1)
                else:
                    row.append(prev[j-1] + prev[j])
            prev = row
            res.append(row)

        return res
