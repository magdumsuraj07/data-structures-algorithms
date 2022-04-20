class Meeting:
    def __init__(self, startTime, endTime) -> None:
        self.startTime = startTime
        self.endTime = endTime

    def __lt__(self, other):
        return self.endTime < other.endTime


class Solution:
    def maximumMeetings(self, n, start, end):
        meetings = []
        for i in range(n):
            meetings.append(Meeting(start[i], end[i]))

        meetings.sort()

        count = 1
        prevMeetingEndTime = meetings[0].endTime
        for i in range(1, n):
            currMeeting = meetings[i]
            if currMeeting.startTime > prevMeetingEndTime:
                count += 1
                prevMeetingEndTime = currMeeting.endTime

        return count
