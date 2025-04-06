class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_nums = dict()

        for i, num in enumerate(nums):
            map_nums[num] = i

        for i, num in enumerate(nums):
            difference = target - num
            if difference in map_nums and map_nums[difference] != i:
                return [i, map_nums[difference]]
            map_nums[num] = i 
