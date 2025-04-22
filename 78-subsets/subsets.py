class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtracking(current_index, out):
            if current_index >= len(nums):
                output.append(out)
                return 

            backtracking(current_index + 1, out)
            backtracking(current_index + 1, out + [nums[current_index]])

        backtracking(0, [])
        return output
        