from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k>0:
            return 1
        
        count, max_count = 0, 0
        original_k = k
        left=0
        right=left
        zero_index_q = deque()

        while(right<len(nums)):
            if nums[right]==0:
                zero_index_q.append(right) 
                if original_k != 0: 
                    if (k==0):
                        zero_index = zero_index_q.popleft()
                        count = right - zero_index
                        left = zero_index+1
                    else:
                        k -= 1
                        count+=1
                else:
                    count=0
            else:
                count +=1

            max_count =  max(max_count, count)
            right+=1

        return max_count

            

            
