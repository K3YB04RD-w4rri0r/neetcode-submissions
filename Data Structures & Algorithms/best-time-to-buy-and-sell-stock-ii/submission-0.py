class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 
        # while strictly increasing keep else sell
        p = 0
        buy_status = False
        buy_index = -1

        for i in range(len(prices) - 1):
            print(prices[i], prices[i+1], buy_status, buy_index)
            if prices[i] >= prices[i + 1]: # strictly decreasing
                if buy_status: # means I have already bought means I have to sell before crash
                    p += (prices[i]  - prices[buy_index])
                    buy_status = False
            else:
                if not buy_status:
                    buy_status = True
                    buy_index = i
                if i + 1 == len(prices) -1:
                    p += (prices[i+1]  - prices[buy_index])
        return p

        