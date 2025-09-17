class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)

        def isFound(mid):
            if nums[mid] >= target:
                return True
            else:
                return False


        while lo < hi:
            mid = (lo + hi)//2
            if isFound(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo



        