class Solution:
    def trap(self, height: List[int]) -> int:
        max_front = [0]*len(height)
        int_max = height[0]
        for i in range(len(height)):
            int_max = max(int_max, height[i])
            max_front[i] = int_max
        print(max_front)

        max_back = [0]*len(height)
        back_max = height[len(height)-1]
        for i in range(len(height)-1, -1, -1):
            back_max = max(back_max, height[i])
            max_back[i] = back_max
        print(max_back)
        
        output = 0
        for i in range(len(height)):
            out = max(0, min(max_front[i], max_back[i]) - height[i]) 
            output += out
        return output
         