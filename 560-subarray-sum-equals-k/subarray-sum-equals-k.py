class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = {0:1}
        count = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            diff = summ - k
            if diff in mapping:
                count += mapping[diff]
            mapping[summ] = mapping.get(summ,0) + 1
        return count
