class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        #define the boundaries for search
        lo = 1
        hi = x

        #loop through the search domain
        while lo < hi:
            sqrt = (lo + hi)//2
            if sqrt*sqrt == x:
                return sqrt
            elif sqrt*sqrt < x:
                lo = sqrt + 1 
            else:
                hi = sqrt
        return lo - 1
