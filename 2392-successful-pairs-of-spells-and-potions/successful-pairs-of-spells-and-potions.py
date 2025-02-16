class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        pairs = [0]*len(spells)
        potions.sort()
        for i,spell in enumerate(spells):
            div = math.ceil(success/spell)
            index = bisect.bisect_left(potions, div)
            pairs[i] = len(potions) - index

            # left = 0
            # right = len(potions)-1
            # while left<=right:
            #     mid = math.floor(int((left+right)/2))
            #     if potions[mid] < div:
            #         left = mid+1
            #     elif potions[mid] == div:
            #         pairs[i] = len(potions)-left
            #         # while mid-1>=0 and potions[mid-1] == div:
            #         #     mid = mid-1
            #         #     pairs[i] +=1
            #         break
            #     elif potions[mid] > div:
            #         pairs[i] = len(potions)-mid
            #         right = mid-1
        
        return pairs