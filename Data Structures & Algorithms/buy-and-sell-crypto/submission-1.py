class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        profit = 0
        finalProfit = 0
        for R in range(1, len(prices)):

            if (prices[R] > prices[L]):
                profit = prices[R] - prices[L]
                finalProfit = max(profit, finalProfit)
            else:
                L = R
        
        return finalProfit

            
