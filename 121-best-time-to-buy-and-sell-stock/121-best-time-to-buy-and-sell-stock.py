class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum_price = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            current_profit = price - minimum_price
            if current_profit > profit:
                profit = current_profit
            minimum_price = min(minimum_price, price)
        return profit