from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #USING MONOTONIC DEQUE (double sided queue)
        result = list()

        main_q = deque() 
        max_q = deque() 
        for i in range(k):
            main_q.append(nums[i])
            while max_q and max_q[-1] < nums[i]:
                max_q.pop()
            max_q.append(nums[i])  
        result.append(max_q[0])  

        for i in range(1, len(nums) - k + 1): 
            front_ele = main_q[0]
            if front_ele == max_q[0]:
                max_q.popleft()
            main_q.popleft()
            new_back_ele = nums[i+k-1] 
            main_q.append(new_back_ele) 
            while max_q and max_q[-1] < new_back_ele:
                max_q.pop()
            max_q.append(new_back_ele)
            result.append(max_q[0])
        return result
#TIME-COMPLEXITY: O(n) 
#SPACE-COMPLEXITY: O(k) 


