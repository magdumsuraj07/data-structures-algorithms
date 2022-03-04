# Question Link :
# https://practice.geeksforgeeks.org/problems/merge-two-binary-max-heap/0

class MaxHeap(object):

    def __init__(self):
        self.heapList = []
        self.currSize = 0

    def __getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def __getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def __getParentIndex(self, childIndex):
        return (childIndex - 1) // 2

    def __hasLeftChild(self, index):
        return self.__getLeftChildIndex(index) < self.currSize

    def __hasRightChild(self, index):
        return self.__getRightChildIndex(index) < self.currSize

    def __hasParent(self, index):
        return self.__getParentIndex(index) >= 0

    def __swap(self, index1, index2):
        self.heapList[index1], self.heapList[index2] = \
            self.heapList[index2], self.heapList[index1]

    def __shiftDown(self, i):
        leftIndex = self.__getLeftChildIndex(i)
        rightIndex = self.__getRightChildIndex(i)
        maxIndex = i

        # Check is leftIndex child of root exists and greater than root
        if (self.__hasLeftChild(i) and
           self.heapList[leftIndex] > self.heapList[maxIndex]):
            maxIndex = leftIndex

        # Check is rightIndex child of root exists and greater than root
        if (self.__hasRightChild(i) and
           self.heapList[rightIndex] > self.heapList[maxIndex]):
            maxIndex = rightIndex

        # If root is not maxIndex, swap maxIndex and continue heapifying
        if maxIndex != i:
            self.__swap(i, maxIndex)
            self.__shiftDown(maxIndex)

    def insert(self, value):
        self.heapList.append(value)
        self.currSize += 1
        self.__shiftUp(self.currSize - 1)

    def deleteMax(self):
        returnValue = self.heapList[0]
        self.__swap(0, self.currSize - 1)
        self.heapList.pop()
        self.currSize -= 1
        self.__shiftDown(0)
        return returnValue

    def getMax(self):
        if self.currSize > 0:
            return self.heapList[0]

    def __shiftUp(self, i):
        while self.__hasParent(i):
            parentIndex = self.__getParentIndex(i)
            if self.heapList[parentIndex] < self.heapList[i]:
                self.__swap(parentIndex, i)
            i = parentIndex

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currSize = len(alist)
        self.heapList = alist[:]

        while (i >= 0):
            self.__shiftDown(i)
            i = i - 1


def mergeHeaps(a, b, n, m):
    newHeapList = a + b
    mx = MaxHeap()
    mx.buildHeap(newHeapList)
    return mx.heapList


if __name__ == '__main__':
    heapA = [10, 5, 6, 2]
    heapB = [12, 7, 9]
    mergedHeap = mergeHeaps(heapA, heapB, len(heapA), len(heapB))
    print(mergedHeap)
