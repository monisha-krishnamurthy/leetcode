class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid = int(len(nums)/2)
        return nums[mid]