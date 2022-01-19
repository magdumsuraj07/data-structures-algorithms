class PriorityQueueNode:
    '''
    Represents node in a priority queue
    '''
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    '''
    Implementation of priority queue using min heap
    '''
    def __init__(self):
        self.pq = []
    
    def getSize(self):
        '''
        Returns size of priority queue
        '''
        return len(self.pq)

    def isEmpty(self):
        '''
        Returns if priority queue is empty or not
        '''
        return self.getSize() == 0

    def getMin(self):
        '''
        Returns value of min element in  priority queue
        '''
        if (self.isEmpty()):
            return None
        return self.pq[0].value

    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            if (self.pq[childIndex].priority < self.pq[parentIndex].priority):
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, value, priority):
        '''
        Insert new node in priority queue
        '''
        pqNode = PriorityQueueNode(value, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        parentIndex = 0
        lChildIndex = (2 * parentIndex) + 1
        rChildIndex = (2 * parentIndex) + 2
        while (lChildIndex < self.getSize()):
            minIndex = parentIndex
            if (self.pq[minIndex].priority > self.pq[lChildIndex].priority):
                minIndex = lChildIndex
            if (rChildIndex < self.getSize() 
               and self.pq[minIndex].priority > self.pq[rChildIndex].priority):
                minIndex = rChildIndex
            
            if (minIndex == parentIndex):
                break
            self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
            parentIndex = minIndex
            lChildIndex = (2 * parentIndex) + 1
            rChildIndex = (2 * parentIndex) + 2
            

    def removeMin(self):
        '''
        Remove node with minimum priority
        '''
        if self.isEmpty():
            return None
        ele = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele