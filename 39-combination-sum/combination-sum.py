class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(current_index, target, out):
            if target == 0:
                combinations.append(out)
                return
            
            if target < 0 or current_index >= len(candidates):
                return 

            backtracking(current_index + 1, target, out)
            backtracking(current_index, target - candidates[current_index], out + [candidates[current_index]])

        out = [] 
        backtracking(0, target, out)
        return combinations