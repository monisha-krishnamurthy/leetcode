class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_nums = dict()
        output = list()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map_nums:
                output.append(i)
                output.append(map_nums[complement])
            map_nums[num] = i 
        return output