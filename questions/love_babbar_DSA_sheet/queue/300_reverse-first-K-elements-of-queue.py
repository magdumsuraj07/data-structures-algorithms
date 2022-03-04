from collections import deque


def modifyQueue(q, k):
    newQueue = deque()
    stack = deque()

    for _ in range(k):
        stack.append(q.pop(0))

    while (stack):
        newQueue.append(stack.pop())
    while (q):
        newQueue.append(q.pop(0))
    return list(newQueue)


if __name__ == '__main__':
    q = [1, 2, 3, 4, 5]
    k = 3
    print(modifyQueue(q, k))
