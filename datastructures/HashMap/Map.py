class MapNode:
    '''
    Represents node of a Map.
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Map:
    '''
    Represents of hash map using seperate chaining.
    '''
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None] * self.bucketSize
        self.count = 0

    def size(self):
        '''
        Returns number of elements existing in map.
        '''
        return self.count

    def getBucketIndex(self, hashCode):
        '''
        Calculates bucket index based on hash code.
        '''
        return (abs(hashCode) % self.bucketSize)

    def insert(self, key, value):
        '''
        Insert new key-value pair into map. If key is already present;
        updates the value
        '''
        hashCode = hash(key)
        index = self.getBucketIndex(hashCode)
        head = self.buckets[index]
        while (head is not None):
            if (head.key == key):
                head.value = value
                return
            head = head.next
        head = self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1

        # Calculate load factor
        loadFactor = self.count/self.bucketSize
        if (loadFactor >= 0.7):
            self.rehash()

    def getValue(self, key):
        '''
        Get value for given key. Returns None if key was not found.
        '''
        hashCode = hash(key)
        index = self.getBucketIndex(hashCode)
        head = self.buckets[index]
        while (head is not None):
            if (head.key == key):
                return head.value
            head = head.next
        return None

    def remove(self, key):
        '''
        Remove key-value pair from map.
        '''
        hashCode = hash(key)
        index = self.getBucketIndex(hashCode)
        head = self.buckets[index]

        if (head is None):
            return None
        prev = None
        while (head is not None):
            if (head.key == key):
                if (prev is None):
                    # Remove head of LL
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                self.count -= 1
                return head.value
            prev = head
            head = head.next
        return None

    def rehash(self):
        '''
        Perform rehashing on map.
        '''
        temp = self.buckets
        self.buckets = [None] * (2 * self.bucketSize)
        self.bucketSize = 2 * self.bucketSize
        self.count = 0
        for head in temp:
            while (head is not None):
                self.insert(head.key, head.value)
                head = head.next
