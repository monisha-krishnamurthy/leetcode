class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)

        def canShipInDdays(capacity):
            day = 1
            capa = capacity
            for weight in weights:
                if weight <= capa:
                    capa = capa - weight 
                else:
                    capa = capacity - weight 
                    day += 1
            if day > days:
                return False
            return True

        while lo < hi:
            capacity = (lo + hi)//2
            if canShipInDdays(capacity) == False:
                lo = capacity + 1
            else:
                hi = capacity
        return lo