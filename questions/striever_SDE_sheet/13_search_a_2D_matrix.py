class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRows = len(matrix)
        nCols = len(matrix[0])
        low = 0
        high = (nRows * nCols) - 1
        while (low <= high):
            mid = (low + high) // 2
            if (matrix[mid//nCols][mid % nCols] == target):
                return True
            if (matrix[mid//nCols][mid % nCols] < target):
                low = mid + 1
            else:
                high = mid - 1

        return False
