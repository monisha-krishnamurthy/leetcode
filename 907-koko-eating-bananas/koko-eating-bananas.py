class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        def canEatAllBananasInHhours(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours > h:
                return False
            return True

        while lo < hi:
            k = (lo + hi) // 2
            if canEatAllBananasInHhours(k) == False:
                lo = k + 1
            else:
                hi = k 
        return lo