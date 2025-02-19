import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hours(piles, rate):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)  # Compute total hours needed
            return hours

        low = 1  # ✅ Minimum possible eating speed
        high = max(piles)  # ✅ Maximum pile size (max eating speed)
        
        while low < high:
            mid = (low + high) // 2
            hours = get_hours(piles, mid)

            if hours > h:
                low = mid + 1  # Increase speed
            else:
                high = mid  # ✅ Instead of `mid - 1`, shrink search space properly
        
        return low  # ✅ `low` now holds the minimum valid eating speed
