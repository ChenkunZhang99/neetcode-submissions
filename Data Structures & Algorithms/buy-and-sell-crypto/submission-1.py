class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_benefit = 0
        min_price = max(prices)
        for price in prices:
            if price < min_price:
                min_price = price
            benefit  = price - min_price
            if benefit > max_benefit:
                max_benefit = benefit
        return max_benefit