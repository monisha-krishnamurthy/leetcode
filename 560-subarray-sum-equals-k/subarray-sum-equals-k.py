class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = {0:1}
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            
            diff = prefix - k
            if diff in mapping:
                count += mapping[diff]
            mapping[prefix] = mapping.get(prefix,0)+1
        return count