class Solution:
    def generateParenthesis(self, n):
        res = [] 

        def valid(s: str):
            open_count = 0
            for ch in list(s):
                open_count += 1 if ch == '(' else -1
                if open_count < 0:
                    return False
            return open_count == 0 

        def dfs(s: str):
            if 2*n == len(s):
                if valid(s):
                    res.append(s)
                return 

            dfs(s + "(")
            dfs(s + ")")

        dfs("")
        return res