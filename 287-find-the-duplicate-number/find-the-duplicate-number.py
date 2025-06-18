class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            index = num - 1
            if nums[abs(num) - 1] < 0:
                return abs(num)
            nums[abs(num) - 1] *= -1
        return -1
 