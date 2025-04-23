class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        res = 0
        leftmax = height[l]
        rightmax= height[r]
        while l < r:
            if leftmax <= rightmax: 
                res += max(0, leftmax - height[l])
                l += 1
                leftmax = max(leftmax, height[l])
            else:
                res += max(0, rightmax - height[r])
                r -= 1
                rightmax = max(rightmax, height[r])
        return res
         