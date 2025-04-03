class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        answer = set()
        for num in nums:
            if num in answer:
                return True
            answer.add(num)

        return False