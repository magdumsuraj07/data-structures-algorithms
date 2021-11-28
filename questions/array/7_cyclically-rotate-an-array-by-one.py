def rotate(arr, n):
    temp = arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = temp
    return arr


if __name__ == '__main__':
    arr = [9, 8, 7, 6, 4, 2, 1, 3]
    arr = rotate(arr, len(arr))
    print(arr)
