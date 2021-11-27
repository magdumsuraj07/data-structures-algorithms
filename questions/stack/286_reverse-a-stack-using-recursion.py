from collections import deque


def insertAtBottom(stack, value):
    """
    Recursive function to insert element at bottom of the stack
    """
    if (len(stack) <= 0):
        stack.append(value)
        return
    ele = stack.pop()
    insertAtBottom(stack, value)
    stack.append(ele)


def reverseStackRecursive(stack):
    """
    Recursive function to reverse a stack
    """
    if (len(stack) <= 0):
        return
    temp = stack.pop()
    reverseStackRecursive(stack)
    insertAtBottom(stack, temp)


# Driver code
if __name__ == '__main__':
    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    reverseStackRecursive(stack)
    print(list(stack))
