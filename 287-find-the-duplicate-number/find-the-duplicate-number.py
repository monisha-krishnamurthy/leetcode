class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        array = [0]*(len(nums) + 1)

        for num in nums:
            if array[num] > 0:
                return num
            array[num] += 1
        return -1
