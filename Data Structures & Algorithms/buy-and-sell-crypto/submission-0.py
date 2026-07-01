class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize min_price to infinity so any first price will be smaller
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # If we find a new lowest price, update our buy day baseline
            if price < min_price:
                min_price = price
            # Otherwise, calculate potential profit and update max_profit if it's better
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit