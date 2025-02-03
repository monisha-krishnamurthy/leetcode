class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        count = 0
        prev_end_time = intervals[0][1]
        for i in intervals[1:]:
            if i[0] < prev_end_time:
                count+=1
            else:
                prev_end_time = i[1]
        return count 
