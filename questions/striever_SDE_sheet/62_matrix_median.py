from sys import maxsize


def getCount(matrix, mid, nRows, nCols):
    """
    Returns count of numbers <= mid
    """
    count = 0
    for r in range(nRows):
        for c in range(nCols):
            if matrix[r][c] <= mid:
                count += 1
            else:
                break

    return count


def getMedian(matrix):
    nRows = len(matrix)
    nCols = len(matrix[0])

    minimum, maximum = maxsize, -1 * maxsize
    for r in range(nRows):
        minimum = min(minimum, matrix[r][0])
        maximum = max(maximum, matrix[r][nCols - 1])

    expectedCount = (nRows * nCols + 1) // 2
    while minimum < maximum:
        mid = minimum + (maximum - minimum) // 2
        count = getCount(matrix, mid, nRows, nCols)
        if count < expectedCount:
            minimum = mid + 1
        else:
            maximum = mid

    return minimum
