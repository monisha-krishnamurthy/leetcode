class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hours(piles, rate):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/rate)
            return hours

        low = 1
        high = max(piles)
        
        while(low < high):
            mid = (low+high)//2
            hours = get_hours(piles, mid)

            if hours > h:
                low = mid + 1
            else:
                high = mid  
            
        return low




        