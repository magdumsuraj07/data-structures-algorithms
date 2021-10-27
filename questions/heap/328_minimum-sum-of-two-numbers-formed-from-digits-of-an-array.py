import heapq


def solve(arr, n):
    heapq.heapify(arr)
    num1 = ''
    num2 = ''

    while True:
        if (len(arr) > 0):
            num1 += str(heapq.heappop(arr))
        else:
            break

        if (len(arr) > 0):
            num2 += str(heapq.heappop(arr))
        else:
            break

    if (num1 == '' and num2 == ''):
        return str(0)
    elif (num1 == ''):
        return num2
    elif (num2 == ''):
        return num1
    else:
        return str(int(num1) + int(num2))


if __name__ == '__main__':
    arr = [5, 3, 0, 7, 4]
    n = len(arr)
    print(solve(arr, n))
