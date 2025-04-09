class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        total = 1
        cnt_zero = 0
        for num in nums:
            if num != 0:
                total *= num
            else:
                cnt_zero += 1

        for i in range(len(nums)):
            if cnt_zero == 0:
                res[i] = total // nums[i]
            else:
                if cnt_zero == 1:
                    if nums[i] != 0:
                        res[i] = 0
                    else:
                        res[i] = total 
                elif cnt_zero > 1:
                    res[i] = 0
        return res 