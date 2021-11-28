def rearrangeElements(arr):
    n = len(arr)
    i = 0
    j = n - 1
    while (i < j):
        while (arr[i] < 0 and i <= n):
            i += 1
        while (arr[j] >= 0 and j >= 0):
            j -= 1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    rearrangeElements(arr)
    print(arr)
