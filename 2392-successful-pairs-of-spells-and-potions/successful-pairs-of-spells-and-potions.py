class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        pairs = [0]*len(spells)
        potions.sort()
        for i,spell in enumerate(spells):
            div = success//spell if success%spell==0 else success//spell+1

            left = 0
            right = len(potions)-1
            while left<=right:
                mid = (left+right)//2
                if potions[mid] < div:
                    left = mid+1
                else:
                    pairs[i] = len(potions)-mid
                    right = mid-1

        return pairs