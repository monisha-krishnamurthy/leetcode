class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        #define the boundaries for search
        lo = 1
        hi = x

        #loop through the search domain
        while lo < hi - 1:
            sqrt = (lo + hi)//2
            if sqrt*sqrt == x:
                return sqrt
            elif sqrt*sqrt < x:
                lo = sqrt
            else:
                hi = sqrt
        return lo
