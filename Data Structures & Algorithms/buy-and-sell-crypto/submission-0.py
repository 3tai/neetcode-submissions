class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 #tracker 
        minBuy = prices[0] #tracker 

        for current in prices: 
            maxProfit = max(maxProfit, current - minBuy)
            minBuy = min(minBuy, current)
        
        return maxProfit 