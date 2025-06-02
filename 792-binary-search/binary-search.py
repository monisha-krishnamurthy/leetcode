class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def recursive(left, right, nums, target):
            if left > right:
                return -1
            mid = (left + right)//2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                return recursive(left, mid-1, nums, target)
            else:
                return recursive(mid+1, right, nums, target)
 
        return recursive(0, n-1, nums, target)


