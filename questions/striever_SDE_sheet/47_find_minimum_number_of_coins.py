denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    remainingAmout = amount
    selectedCoins = []
    i = len(denominations) - 1
    while remainingAmout > 0:
        if denominations[i] <= remainingAmout:
            remainingAmout -= denominations[i]
            selectedCoins.append(denominations[i])
        else:
            i -= 1

    return len(selectedCoins)
