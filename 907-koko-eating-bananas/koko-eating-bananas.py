class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        speed = max(piles)

        while left <= right:
            mid = (left + right)//2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/mid)
            if totalTime > h:
                left = mid + 1
            elif totalTime <= h:
                speed = min(speed, mid)
                right = mid - 1
        return speed
#TIME-COMPLEXITY: O(m*n), n is the length of the input array and m is the maximum number of bananas in a pile.
#SPACE-COMPLEXITY: O(1)
