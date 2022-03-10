class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose a matrix
        for r in range(n):
            for c in range(n):
                if r < c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reverse each row in matrix
        for row in matrix:
            row.reverse()
