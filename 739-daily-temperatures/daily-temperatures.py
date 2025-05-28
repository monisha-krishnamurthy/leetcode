class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)

        stack.append((temperatures[0],0))
        for i in range(1, len(temperatures)):
            if temperatures[i] > stack[-1][0]:
                answer[stack[-1][1]] = i - stack[-1][1] 
                stack.pop()
            while stack and temperatures[i] > stack[-1][0]:
                answer[stack[-1][1]] = i - stack[-1][1] 
                stack.pop()

            stack.append((temperatures[i], i))
        return answer

