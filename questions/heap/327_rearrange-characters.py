from collections import Counter
import math


def rearrangeCharacters(s):
    n = len(s)
    c = Counter(s).most_common()

    if (c[0][1] <= math.ceil(n/2)):
        return 1
    else:
        return 0


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input()
        print(rearrangeCharacters(s))
