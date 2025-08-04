class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        count.sort()
        maxFreq = count[25]
        idleTime = (maxFreq - 1) * n
        for i in range(24, -1, -1):
            idleTime -= min(maxFreq - 1, count[i]) 
        return max(0, idleTime) +  len(tasks)


