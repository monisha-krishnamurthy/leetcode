class Solution:
    #USING DYNAMIC PROGRAMMING
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        n = len(temperatures)

        for i in range(n-2, -1, -1):
            j = i + 1
            while j<n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]

            if j < n:
                res[i] = j - i
        return res
#TIME-COMPLEXITY: O(n)
#SPACE-COMPLEXITY: O(n)



