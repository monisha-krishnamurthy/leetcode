class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        candidate = nums[0]

        for ele in nums:
            if ele == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = ele
                    count = 1
        return candidate