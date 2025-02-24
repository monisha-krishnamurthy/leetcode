class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 2 1 5 0 4 6 
        # 0 1 2 4 5 6
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
