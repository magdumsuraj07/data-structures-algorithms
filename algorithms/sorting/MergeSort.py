def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    temp = []

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # Copy remaining elements of first array to temp
    while i <= mid:
        temp.append(arr[i])
        i += 1

    # Copy remaining elements of second array to temp
    while j <= high:
        temp.append(arr[j])
        j += 1

    # Copy elements back to arr
    for k in range(low, high + 1):
        arr[k] = temp[k - low]


def mergeSort(arr, low, high):
    if low == high:
        return

    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)
