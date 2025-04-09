class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using prefix and suffix arrays
        res = [0]*len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i] 
        return res 
        
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

