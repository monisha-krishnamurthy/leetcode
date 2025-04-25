import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum = sys.maxsize
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            profit = prices[i] - minimum
            max_profit = max(max_profit, profit)
        return max_profit