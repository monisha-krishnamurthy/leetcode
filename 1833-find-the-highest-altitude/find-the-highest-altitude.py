class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum =[0]*len(gain)
        prefix_sum[0] =gain[0]
        if len(gain)==1:
            return max(gain[0],0)
        for i in range(1,len(gain)):
            prefix_sum[i] = prefix_sum[i-1] + gain[i]
        print(prefix_sum)

        return max(max(prefix_sum),0)
