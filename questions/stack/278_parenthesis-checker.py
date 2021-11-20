from collections import deque


def getKey(d, val):
    for key, value in d.items():
        if val == value:
            return key


def ispar(x):
    stack = deque()
    pairs = dict({'{': '}', '[': ']', '(': ')'})

    for ch in list(x):
        if ch in pairs.keys():
            stack.append(ch)
        elif len(stack) > 0 and stack[-1] == getKey(pairs, ch):
            stack.pop()
        else:
            return False

    if (len(stack) == 0):
        return True
    else:
        return False


if __name__ == '__main__':
    x = '{[()]}'
    print(ispar(x))
