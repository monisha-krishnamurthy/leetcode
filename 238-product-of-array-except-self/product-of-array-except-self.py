class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        prefix = 1
        for i in range(1,n):
            prefix = prefix * nums[i-1]
            res[i] *= prefix
        print(res)

        suffix = 1
        for j in range(n-2, -1, -1):
            suffix = suffix * nums[j+1]
            res[j] *= suffix 
        print(res)

        return res

