class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        no_of_ones=0
        ones = []
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                no_of_ones += 1
                ones.append(i)
        no_of_even_places = int((len(flowerbed)/2)) if len(flowerbed)%2==0 else int((len(flowerbed)/2))+1
        if no_of_ones == 0:
            if no_of_even_places >= n:
                return True
            else:
                return False
        else:
            first_zeroes = ones[0] + 1
            if first_zeroes%2==0:
                no_of_evens = int(first_zeroes/2)  
            else:
                no_of_evens = int(first_zeroes/2) + 1
            if ones[0]%2==0:
                n = n - no_of_evens + 1
            else:
                n = n - first_zeroes + no_of_evens + 1
            for i in range(len(flowerbed)):
                flag1 = False
                flag2 = False
                if flowerbed[i] == 1:
                    if i+2 < len(flowerbed):
                        if flowerbed[i+2] == 0:
                            flag1 = True
                    if i+3 < len(flowerbed):
                        if flowerbed[i+3] == 0:
                            flag2 = True
                    else:
                        flag2 = True 
                    if flag1 and flag2:
                        flowerbed[i+2] = 1
                        n -= 1
            if n>0:
                return False
            else:
                return True
            

                            
        
