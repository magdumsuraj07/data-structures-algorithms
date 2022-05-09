class Solution:
    def findPathsHelper(self, grid, n, row, col, path, visited, res):
        if (
            row >= n
            or row < 0
            or col >= n
            or col < 0
            or grid[row][col] == 0
            or visited[row][col] is True
        ):
            return

        visited[row][col] = True

        if row == n - 1 and col == n - 1:
            res.append(path)
            visited[row][col] = False
            return

        # Check down
        self.findPathsHelper(grid, n, row + 1, col, path + "D", visited, res)

        # Check left
        self.findPathsHelper(grid, n, row, col - 1, path + "L", visited, res)

        # Check right
        self.findPathsHelper(grid, n, row, col + 1, path + "R", visited, res)

        # Check up
        self.findPathsHelper(grid, n, row - 1, col, path + "U", visited, res)

        visited[row][col] = False

    def findPaths(self, grid, n):
        visited = [[False for c in range(n)] for r in range(n)]
        res = []
        self.findPathsHelper(grid, n, 0, 0, "", visited, res)
        return res
