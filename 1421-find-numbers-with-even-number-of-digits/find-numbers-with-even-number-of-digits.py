class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if self.count_digits(num) % 2 == 0:
                result += 1
        return result
    
    def count_digits(self, number: int) -> int:
        digits = 0
        while number > 0:
            number = number // 10
            digits += 1
        return digits

