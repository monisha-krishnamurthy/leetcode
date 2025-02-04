class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        points.sort(key= lambda x:x[1])
        prev_end_coord = points[0][1]
        for i in points[1:]:
            if i[0] <= prev_end_coord:
                count +=1
            else:
                prev_end_coord = i[1]
        return len(points)-count

        #         if set(i).intersection(set(j)) != 'Null':
        #             count +=1
        # return count
                  