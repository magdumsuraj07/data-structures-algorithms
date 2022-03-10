class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prevStart = res[-1][0]
            prevEnd = res[-1][1]
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            if prevEnd >= currStart:
                res[-1][0] = min(prevStart, currStart)
                res[-1][1] = max(prevEnd, currEnd)
            else:
                res.append(intervals[i])
        return res
