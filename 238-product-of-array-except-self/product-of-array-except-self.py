class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        prod = 1
        for i in range(len(nums)):
            prod = prod * nums[i]
            prefix[i] = prod
        print(prefix)

        prod = 1
        for j in range(len(nums)-1, -1, -1):
            prod = prod * nums[j]
            suffix[j] = prod
        print(suffix)

        answer = [0]*len(nums)
        for i in range(len(nums)):
            if(i==0):
                answer[i] = suffix[i+1]
            elif(i==len(nums)-1):
                answer[i] = prefix[i-1]
            else:
                answer[i] = prefix[i-1] * suffix[i+1]
        return answer


        
        