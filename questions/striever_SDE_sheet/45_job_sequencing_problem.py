class Solution:
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda job: job.profit, reverse=True)

        maxDeadline = -1
        for job in Jobs:
            if job.deadline > maxDeadline:
                maxDeadline = job.deadline

        result = [-1 for i in range(maxDeadline + 1)]
        jobCount = jobProfit = 0
        for i in range(len(Jobs)):
            for j in range(Jobs[i].deadline, 0, -1):
                if result[j] == -1:
                    result[j] = Jobs[i].id
                    jobCount += 1
                    jobProfit += Jobs[i].profit
                    break

        return (jobCount, jobProfit)
