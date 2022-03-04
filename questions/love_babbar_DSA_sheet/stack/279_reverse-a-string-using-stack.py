from collections import deque


def reverse(s):
    stack = deque()
    for ch in s:
        stack.append(ch)

    reversedString = ''
    while(stack):
        reversedString += stack.pop()

    return reversedString


if __name__ == '__main__':
    s = "GeeksforGeeks"
    print(reverse(s))
