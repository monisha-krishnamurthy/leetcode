class Solution:
    #UPPER BOUND
#Boundary searches refer to finding the first or last occurrence of a target value in a sorted list, while insert-point calculations refer to determining where a new value should be inserted to maintain sorted order, even if the value isn’t already present. Using binary search with "right = len(nums)" and treating the right bound as exclusive makes these operations easier because it naturally handles edge cases, like inserting beyond the last element or stopping exactly at the correct boundary, without running into off-by-one errors, since right can point just past the last index without breaking. This approach is especially useful when you need precise control over positions rather than just checking if a value exists.
    def search(self, nums: List[int], target: int) -> int:
        left  = 0
        right = len(nums)

        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] > target:
                right = mid
            elif nums[mid] <= target:
                left = mid + 1
        return left-1 if (left and nums[left-1] == target) else -1

#TIME-COMPLEXITY: O(logN)
#SPACE-COMPLEXITY: O(1)


