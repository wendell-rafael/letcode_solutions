class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            atual_profit = prices[j] - prices[i]
            if prices[i] < prices[j]:
                max_profit = max(atual_profit, max_profit)
            else:
                i = j
            j += 1
        return (max_profit)