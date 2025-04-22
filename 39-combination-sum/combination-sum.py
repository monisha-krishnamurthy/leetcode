class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def backtracking(current_index, target, out):
            if target == 0:
                combinations.append(out)
                return
            
            if current_index >= len(candidates):
                return 

            if target >= candidates[current_index]:
                backtracking(current_index + 1, target, out)
                backtracking(current_index, target - candidates[current_index], out + [candidates[current_index]])

        out = [] 
        backtracking(0, target, out)
        return combinations