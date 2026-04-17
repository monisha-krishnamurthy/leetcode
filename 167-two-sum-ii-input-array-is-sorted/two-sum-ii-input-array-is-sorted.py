class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = {}
        for i,num in enumerate(numbers):
            compliment = target - num
            if compliment in mapping:
                return [mapping.get(compliment,0)+1, i+1]
            mapping[num] = i
        