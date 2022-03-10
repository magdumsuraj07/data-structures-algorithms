class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            # If second array is empty; return
            return
        for i in range(m):
            if nums1[i] > nums2[0]:
                nums1[i], nums2[0] = nums2[0], nums1[i]

                # Insert first element at correct position
                first = nums2[0]
                k = 1
                while k < n and nums2[k] < first:
                    nums2[k - 1] = nums2[k]
                    k += 1
                nums2[k - 1] = first

        # Copy elements of second array to end of first array
        for i in range(n):
            nums1[m + i] = nums2[i]
