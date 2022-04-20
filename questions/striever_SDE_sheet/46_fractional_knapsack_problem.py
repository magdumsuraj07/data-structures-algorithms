class Solution:
    def fractionalknapsack(self, W, Items, n):
        # Sort the items in decreasing order of value/weight ratio
        Items.sort(key=lambda x: x.value / x.weight, reverse=True)

        currWeight = 0
        maxValue = 0
        for item in Items:
            if currWeight + item.weight <= W:
                # Current item can be included completely
                currWeight += item.weight
                maxValue += item.value
            else:
                # Include current item partially
                remainingWeight = W - currWeight
                maxValue += remainingWeight * (item.value / item.weight)
                break

        return maxValue
