class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==1:
            return nums[0]
        summ=0
        for i in range(k):
            summ += nums[i]
        left = 0
        right = k-1
        max_sum = summ
        while(right<len(nums)-1):
            right +=1
            summ = summ - nums[left] + nums[right]
            max_sum = max(max_sum, summ)
            left +=1
        return (max_sum/k)

            