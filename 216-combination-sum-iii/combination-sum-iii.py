class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        if k>n:
            return []
        
        def combinations(k, n, digits, output_set, output=[]):
            if n == 0 and k == 0:
                output.sort()
                output_set.add(tuple(output))
                return
            elif (n !=0 and k==0) or (n==0 and k!=0):
                return 

            for digit in digits:
                if digit <= n:
                    combinations(k-1, n-digit, digits-{digit}, output_set, output+[digit])

        output_set = set()
        combinations(k, n, digits, output_set)
        return list(output_set)
            