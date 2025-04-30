class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            str_num = str(num)
            if len(str_num) % 2 == 0:
                    count = count + 1
        return count