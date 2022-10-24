'''
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        # If there is only one day, the profit will be zero
        if len(prices) > 1:
            # Use two pointers to find the max profit
            left, right = 0, 1
            while right < len(prices):
                profit = prices[right] - prices[left]
                if profit < 0:
                    left = right
                else:
                    max_profit = max(max_profit, profit)
                right += 1

        return max_profit        