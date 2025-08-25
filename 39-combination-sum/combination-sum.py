class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(current_index, total, out):
            if total == target:
                combinations.append(out.copy())
                return 

            if current_index >= len(candidates) or total>target:
                return

            out.append(candidates[current_index])
            backtracking(current_index, total + candidates[current_index], out)
            out.pop()
            backtracking(current_index + 1, total, out)

        backtracking(0, 0, [])
        return combinations