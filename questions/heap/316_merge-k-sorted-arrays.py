
class MinHeap(object):
    def __init__(self):
        self.heapList = []
        self.size = 0

    def swap(self, indexA, indexB):
        self.heapList[indexA], self.heapList[indexB] = \
            self.heapList[indexB], self.heapList[indexA]

    def minHeapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2

        smallest = index
        if left < self.size and self.heapList[left] < self.heapList[smallest]:
            smallest = left

        if (right < self.size
           and self.heapList[right] < self.heapList[smallest]):
            smallest = right

        if index != smallest:
            self.swap(index, smallest)
            self.minHeapify(smallest)

    def buildHeap(self, arr):
        self.heapList = arr[:]
        self.size = len(arr)

        for i in range(self.size//2, -1, -1):
            self.minHeapify(i)


class HeapNode(object):
    def __init__(self, data, indexI, indexJ):
        self.data = data
        self.indexI = indexI
        self.indexJ = indexJ

    def __lt__(self, other):
        return self.data < other.data


def mergeKArrays(arr, K):
    minHeap = MinHeap()
    resultSize = 0
    # Create a heap, push first element of every array into heap
    # calculate size of result array
    heapElements = []
    for i in range(len(arr)):
        heapElements.append(HeapNode(arr[i][0], i, 0))
        resultSize += len(arr[i])

    minHeap.buildHeap(heapElements)

    resultArray = []
    for k in range(resultSize):
        minNode = minHeap.heapList[0]
        resultArray.append(minNode.data)

        if minNode.indexJ < len(arr[minNode.indexI])-1:
            minNode.data = arr[minNode.indexI][minNode.indexJ + 1]
            minNode.indexJ = minNode.indexJ + 1
            minHeap.minHeapify(0)
        else:
            minNode.data = float('inf')
            minHeap.minHeapify(0)
    return resultArray


if __name__ == '__main__':
    arr = [[1, 2, 3, 4],
           [2, 2, 3, 4],
           [5, 5, 6, 6],
           [7, 8, 9, 9]]

    # mergeKArrays(arr, K=4)
    print(mergeKArrays(arr, K=4))
