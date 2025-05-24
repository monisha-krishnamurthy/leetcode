class Solution:
    #USING STACKS
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop() 
            if token not in '+-*/':
                return int(token)

            right = dfs()
            left = dfs()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)
        return dfs()

#NOTE: Truncation toward zero always removes the decimal part to bring the number closer to zero, while floor division rounds the number down to the nearest integer, moving toward negative infinity.
#TIME-COMPLEXITY: O(n)
#SPACE-COMPLEXITY: O(n)