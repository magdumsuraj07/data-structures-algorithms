def isSubset( a1, a2, n, m):
    setA1 = set(a1)
    setA2 = set(a2)
    if (setA2.issubset(setA1)):
        return "Yes"
    else:
        return "No"