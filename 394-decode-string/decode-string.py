# 3[abc2[d]] = [3 -- [--a--b--c--2--[--d--]---]]

class Solution:
    def decodeString(self, s: str) -> str:
        stack_incoming = []
        intermediate_string = ""
        numbers = {'0','1','2','3','4','5','6','7','8','9'}

        i=0
        while i<len(s):
            if(s[i] == ']'):
                char = stack_incoming.pop()
                while char != '[':
                    intermediate_string = char + intermediate_string 
                    char = stack_incoming.pop()

                num = stack_incoming.pop()
                iterations = num
                # print(iterations, "11")
                while stack_incoming and stack_incoming[-1] in numbers:
                    num = stack_incoming.pop()
                    iterations = num + iterations 
                # print(iterations, "iter")

                for it in range(int(iterations)):
                    duplicate_str = list(intermediate_string)
                    stack_incoming.extend(duplicate_str)
  
                intermediate_string = ""         
            else:
                stack_incoming.append(s[i])
            i +=1

        return ''.join(stack_incoming)


