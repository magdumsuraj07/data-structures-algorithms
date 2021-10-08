def heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i  # Initialize largest as root

    # Check if left child exists and greater than largest
    if (left < n and arr[left] > arr[largest]):
        largest = left

    # Check if right child exists and greater than largest
    if (right < n and arr[right] > arr[largest]):
        largest = right

    # Change the root if needed
    if (largest != i):
        arr[largest], arr[i] = arr[i], arr[largest]  # Swap

        # Heapify the root
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
