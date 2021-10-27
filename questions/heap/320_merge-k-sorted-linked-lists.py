
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
        if (left < self.size
           and self.heapList[left].data < self.heapList[smallest].data):
            smallest = left

        if (right < self.size
           and self.heapList[right].data < self.heapList[smallest].data):
            smallest = right

        if index != smallest:
            self.swap(index, smallest)
            self.minHeapify(smallest)

    def pop(self):
        returnValue = self.heapList[0]
        self.heapList[0] = self.heapList[self.size - 1]
        self.heapList.pop()
        self.size -= 1
        self.minHeapify(0)
        return returnValue

    def buildHeap(self, arr):
        self.heapList = arr[:]
        self.size = len(arr)

        for i in range(self.size//2, -1, -1):
            self.minHeapify(i)


class Node(object):
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next


def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk = walk.next
    print()


def mergeKLists(arr, K):
    heap = MinHeap()
    heap.buildHeap(arr)
    resList = LinkedList()

    while (len(heap.heapList) > 0):
        minNode = heap.heapList[0]
        resList.add(minNode.data)
        if minNode.next is None:
            heap.pop()
        else:
            heap.heapList[0] = minNode.next
            heap.minHeapify(0)

    return resList.head


if __name__ == '__main__':
    linkedList1 = LinkedList()
    linkedList1.add(1)
    linkedList1.add(2)
    linkedList1.add(3)

    linkedList2 = LinkedList()
    linkedList2.add(4)
    linkedList2.add(5)

    linkedList3 = LinkedList()
    linkedList3.add(5)
    linkedList3.add(6)

    linkedList4 = LinkedList()
    linkedList4.add(7)
    linkedList4.add(8)

    K = 4
    arr = [linkedList1.head, linkedList2.head,
           linkedList3.head, linkedList4.head]
    newHead = mergeKLists(arr, K)
    printList(newHead)
