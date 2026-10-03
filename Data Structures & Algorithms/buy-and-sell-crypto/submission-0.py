class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit=0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if (prices[j]-prices[i])>highest_profit:
                    highest_profit=prices[j]-prices[i]
        return highest_profit
                 