class Solution:
    #TOP DOWN APPROACH i.e., MEMOIZATION
    def climbStairs(self, n: int) -> int:
        cache = [-1]*n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]

        return dfs(0)   #how does it internally compute everything to finally give the
                        #output at dfs(0)

"""
dfs(0)
├── dfs(1)
│   ├── dfs(2)
│   │   ├── dfs(3) → 1
│   │   └── dfs(4) → 0
│   │   → cache[2] = 1
│   └── dfs(3) → 1
│   → cache[1] = 2
└── dfs(2) → cache hit → 1

→ cache[0] = 3
"""


        