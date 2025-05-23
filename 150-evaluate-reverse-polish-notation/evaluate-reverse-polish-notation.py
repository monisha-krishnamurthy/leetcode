class Solution:
    #BRUTE-FORCE SOLUTION 
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens)>1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    right_operand = int(tokens[i-1])
                    left_operand = int(tokens[i-2])
                    if tokens[i] == "+":
                        result = left_operand + right_operand 
                    elif tokens[i] == "-":
                        result = left_operand - right_operand
                    elif tokens[i] == "*":
                        result = left_operand * right_operand
                    elif tokens[i] == "/":
                        result = int(left_operand / right_operand) 
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:] #focus
                    break 
        return int(tokens[0])


#NOTE: Truncation toward zero always removes the decimal part to bring the number closer  to zero, while floor division rounds the number down to the nearest integer, moving toward negative infinity.
#TIME-COMPLEXITY: O(n^2)
#SPACE-COMPLEXITY: O(n^2)  