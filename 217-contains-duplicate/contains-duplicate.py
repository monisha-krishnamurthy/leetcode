class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        answer = set()
        for i in nums:
            answer.add(i)

        if len(answer) == len(nums):
            return False
        return True