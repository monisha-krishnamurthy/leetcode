class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = dict()
        for i in range(len(nums)):
            mapping[nums[i]]= mapping.get(nums[i], 0) + 1
        for i in mapping.values():
            if i > 1:
                return True
        return False