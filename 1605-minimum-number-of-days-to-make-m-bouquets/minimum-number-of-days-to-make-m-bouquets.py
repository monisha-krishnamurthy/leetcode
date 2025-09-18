class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < k*m:
            return -1 

        lo = 1
        hi = max(bloomDay) 
            
        def canMakeMBouquets(mid):
            noOfBouquets = 0
            flowers = 0
            index = 0
            while noOfBouquets < m and index < len(bloomDay):
                if bloomDay[index] <= mid:
                    flowers +=1
                    if flowers == k:
                        noOfBouquets += 1
                        flowers = 0
                    index += 1
                    continue
                else:
                    flowers = 0
                    index += 1
            if noOfBouquets >= m:
                return True
            else:
                return False


        while lo < hi:
            mid = (lo+hi)//2
            if canMakeMBouquets(mid) == False:
                lo = mid + 1
            else:
                hi = mid
        return lo