class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = defaultdict(int)
        for i, num in enumerate(numbers):
            search = target - num
            if search in dictionary:
                return [dictionary[search], i+1]
            dictionary[num] = i + 1
        return []
            
            


