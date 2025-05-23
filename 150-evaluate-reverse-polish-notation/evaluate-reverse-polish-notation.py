class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in range(len(tokens)):
            if tokens[i] not in ('+', '-', '/', '*'): 
                stack.append(int(tokens[i])) 
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = 0
                if tokens[i] == "+":
                    result = operand2 + operand1
                elif tokens[i] == "-":
                    result = operand2 - operand1
                elif tokens[i] == "*":
                    result = operand2 * operand1
                elif tokens[i] == "/":
                    #Truncation toward zero always removes the decimal part to bring the number closer to zero, while floor division rounds the number down to the nearest integer, moving toward negative infinity.
                    result = int(operand2 / operand1)
                stack.append(result) 
        return stack[-1] 