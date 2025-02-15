class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if k>n:
            return []
        
        def combinations(k, n, digits_index, digits, output_list, output=[]):
            if n == 0 and k == 0:
                output_list.append(output)
                return
            elif (n !=0 and k==0) or (n==0 and k!=0):
                return 

            for index in range(digits_index, 9):
                digit = digits[index]
                if digit <= n:
                    combinations(k-1, n-digit, index+1, digits, output_list, output+[digit])

        output_list = []
        combinations(k, n, 0, digits, output_list, [])
        return output_list
            