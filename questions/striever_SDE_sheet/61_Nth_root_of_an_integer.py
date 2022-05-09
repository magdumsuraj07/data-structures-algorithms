from decimal import Decimal


def findNthRootOfM(n, x):
    # Write your Code here.
    x = Decimal(x)
    n = Decimal(n)
    if x >= 0 and x <= 1:
        low = x
        high = 1
    else:
        low = 1
        high = x

    # used for taking approximations
    # of the answer
    epsilon = Decimal(10**-7)

    # Do binary search
    guess = Decimal((low + high) / 2)
    while abs(guess**n - x) >= epsilon:
        if guess**n > x:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
    return "{:.6f}".format(guess)
