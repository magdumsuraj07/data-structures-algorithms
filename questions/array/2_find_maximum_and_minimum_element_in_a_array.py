from sys import maxsize

def getMinMax( a, n):
    minimum = maxsize
    maximum = -1 * maxsize
    for num in a:
        if (num < minimum):
            minimum = num
        if (num > maximum):
            maximum = num
    return minimum, maximum