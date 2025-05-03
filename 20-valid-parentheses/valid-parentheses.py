class Solution:
    #USING STACKS 
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")" : "(", "]" : "[", "}" : "{"}
        
        if len(s) == 1:
            return False

        for ch in s:
            if ch in mapping:   #to avoid all other invalid cases such as "){" or "}"
                if stack and stack[-1] == mapping[ch]: #it is imp to have 2 nested loops
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch) 
        return True if not stack else False
#TIME-COMPLEXITY: O(n)
#SPACE-COMPLEXITY: O(n)


        