class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        return len(nums_set) != len(nums) 