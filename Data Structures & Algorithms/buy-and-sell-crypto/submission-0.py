class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pr = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_pr = max(max_pr, prices[j] - prices[i])

        return max_pr