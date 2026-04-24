class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left+right)//2
            count, total = 0, 1
            for weight in weights:
                if count + weight > mid:
                    total += 1
                    count = 0
                count += weight
            if total <= days:
                right = mid
            else:
                left = mid + 1
        return left