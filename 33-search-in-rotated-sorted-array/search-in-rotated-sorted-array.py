class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        def binary_search(left: int, right: int):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        result = binary_search(0, pivot-1)
        if result != -1:
            return result
        return binary_search(pivot, len(nums)-1) 






    