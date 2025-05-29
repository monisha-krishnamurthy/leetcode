class Solution:
    #USING STACK
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_val, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append((temp, i))                
        return result
#TIME-COMPLEXITY: O(n^2)
#SPACE-COMPLEXITY: O(n)



