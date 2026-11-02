class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            #Wenn wir einen günstigeren Kaufpreis finden, merken wir uns diesen
            if price < min_price:
                min_price = price
            #Schauen ob wir den Gewinn vergrößern können
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit