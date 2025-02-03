class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left_plot = (i==0) or (flowerbed[i-1]==0)
                empty_right_plot = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
            
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    n -= 1
        if n>0:
            return False
        else:
            return True


                            
        
