class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # for i in range(len(flowerbed)):
        #     if flowerbed[i] == 0:
        #         empty_left_plot = (i==0) or (flowerbed[i-1]==0)
        #         empty_right_plot = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
            
        #         if empty_left_plot and empty_right_plot:
        #             flowerbed[i] = 1
        #             n -= 1
        # if n>0:
        #     return False
        # else:
        #     return True

        if n==0:
            return True
        elif len(flowerbed)==1 and flowerbed[0]==0:
            return True

        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[0] == 0 and flowerbed[1] ==0:
                count +=1
                flowerbed[0] = 1
                print(flowerbed)
                print(count, "1st")
            if (i>0 and i<len(flowerbed)-1) and flowerbed[i]==0:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    count +=1
                    print(count, "2nd")
                    continue
            if flowerbed[-1] ==0 and flowerbed[-2]==0:
                count +=1
                flowerbed[-1] = 1
                print(flowerbed)
                print(count, "3rd")

        if count >= n:
            return True
        else:
            return False

                            
        
