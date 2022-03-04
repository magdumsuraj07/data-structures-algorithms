from collections import Counter
import math


def reorganizeString(s):
    n = len(s)
    c = Counter(s).most_common()

    if (c[0][1] <= math.ceil(n/2)):
        charSeq = []
        for ch, count in c:
            charSeq.extend([ch] * count)

        result = [None] * n
        for i in range(0, n, 2):
            result[i] = charSeq.pop(0)
        for i in range(1, n, 2):
            result[i] = charSeq.pop(0)

        return ''.join(result)
    else:
        return ""


if __name__ == '__main__':
    s = "abbabababbabbbaabaaaaabbbbabbbbbababbbabbabbb"
    print(reorganizeString(s))
