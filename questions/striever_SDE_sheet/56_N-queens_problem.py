class Solution:
    def isSafe(self, row, col, board, n):
        # Check for same column
        for r in range(row):
            if board[r][col] == "Q":
                return False

        # Check for diagonal (upward-left)
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r, c = r - 1, c - 1

        # Check for diagonal (upward-right)
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r, c = r - 1, c + 1

        return True

    def solveNQueens(self, n):
        board = [["." for c in range(n)] for r in range(n)]
        res = []

        def backtrack(row, n):
            if row == n:
                temp = []
                for r in range(n):
                    temp.append("".join(board[r]))
                res.append(temp)
                return

            for col in range(n):
                if self.isSafe(row, col, board, n):
                    board[row][col] = "Q"
                    backtrack(row + 1, n)
                    board[row][col] = "."

        backtrack(0, n)
        return res
