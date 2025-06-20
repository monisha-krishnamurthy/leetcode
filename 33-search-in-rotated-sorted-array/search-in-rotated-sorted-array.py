class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]: #left sorted array
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: #right sorted array
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


