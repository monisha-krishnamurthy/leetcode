class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        i, j = 0, len(height)-1

        while i<j:
            water = (j-i) * min(height[i], height[j])
            max_water = max(water, max_water)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water
        