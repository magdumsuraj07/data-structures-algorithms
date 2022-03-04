class Stack(object):
    """
    Stack class implementation using list.
    """
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)


# Recursice function to insert element at bottom of stack
def insertAtBottom(st, data):
    if (st.isEmpty()):
        st.push(data)
    else:
        ele = st.pop()
        insertAtBottom(st, data)
        st.push(ele)


if __name__ == '__main__':
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    insertAtBottom(st, 4)
    print(st._items)
