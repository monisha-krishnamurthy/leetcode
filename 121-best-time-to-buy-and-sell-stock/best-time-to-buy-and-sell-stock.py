class Solution:
    #USING DYNAMIC PROGRAMMING
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minBuy = prices[0]

        #same logic as the sliding window solution
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i]-minBuy)
            minBuy = min(minBuy, prices[i])        
        return max_profit
#TIME-COMPLEXITY: O(n)
#SPACE-COMPLEXITY: O(1)

