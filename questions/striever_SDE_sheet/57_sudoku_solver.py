class Solution:
    def isSafe(self, row, col, num, board):
        for i in range(len(board)):
            if board[i][col] == num:
                return False

            if board[row][i] == num:
                return False

            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    for num in range(1, 10):
                        num = str(num)
                        if self.isSafe(r, c, num, board):
                            board[r][c] = num

                            if self.solveSudoku(board):
                                return True
                            else:
                                board[r][c] = "."
                    return False
        return True
