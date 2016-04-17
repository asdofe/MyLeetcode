class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        my_profit = 0
        for index, price in enumerate(prices):
            if index == 0:
                continue
            my_profit += max(price - prices[index-1], 0)
            
                
                
        return my_profit
        