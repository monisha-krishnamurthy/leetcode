class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setNums = set()

        for i in range(len(nums)):
            if nums[i] in setNums:
                return nums[i]
            setNums.add(nums[i])
        return 0