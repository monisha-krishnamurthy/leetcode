class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = defaultdict(int)
        for i in range(len(numbers)):
            search = target - numbers[i]
            if search in dictionary:
                return [dictionary[search], i+1]
            dictionary[numbers[i]] = i + 1
        return []
            
            


