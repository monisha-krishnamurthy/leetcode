class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < k*m:
            return -1 

        lo = 1
        hi = max(bloomDay) 
            
        def canMakeMBouquets(mid):
            bouquets = 0
            flowers = 0
            for day in bloomDay:
                if day <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        while lo < hi:
            mid = (lo+hi)//2
            if canMakeMBouquets(mid) == False:
                lo = mid + 1
            else:
                hi = mid
        return lo