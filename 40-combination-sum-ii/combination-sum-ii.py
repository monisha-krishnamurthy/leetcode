class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def backtracking(index, total, out):
            if total == target:
                combinations.append(out.copy())
                return

            if total > target or index >= len(candidates):
                return

            out.append(candidates[index])
            backtracking(index + 1, total + candidates[index], out)
            out.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            backtracking(index + 1, total, out)

        backtracking(0, 0, [])
        return combinations

