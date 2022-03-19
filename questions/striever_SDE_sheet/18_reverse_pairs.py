class Solution:
    def merge(self, nums, low, mid, high):
        i = low
        j = mid + 1

        # Count pairs
        count = 0
        while i <= mid:
            while (j <= high) and (nums[i] > (2 * nums[j])):
                j += 1
            count = count + (j - (mid + 1))
            i += 1

        # Merge functionality
        temp = []
        i = low
        j = mid + 1
        while i <= mid and j <= high:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        # Copy remaining elements of left array to temp
        while i <= mid:
            temp.append(nums[i])
            i += 1

        # Copy remaining elements of right array to temp
        while j <= high:
            temp.append(nums[j])
            j += 1

        # Copy all elements back to nums array
        for i in range(low, high + 1):
            nums[i] = temp[i - low]

        return count

    def mergeSort(self, nums, low, high):
        if low == high:
            return 0

        mid = (low + high) // 2
        pairsCount = self.mergeSort(nums, low, mid)
        pairsCount += self.mergeSort(nums, mid + 1, high)

        pairsCount += self.merge(nums, low, mid, high)

        return pairsCount

    def reversePairs(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        return self.mergeSort(nums, low, high)
