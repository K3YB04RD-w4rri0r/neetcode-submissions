class Solution:
    def total_time(self, piles, k):
        sm = 0
        for p in piles:
            sm += p//k
            sm = sm + 1 if p%k != 0 else sm
        return sm
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_k = 1
        high_k = max(piles) + 1
        while low_k < high_k:
            mid_k = (high_k + low_k)//2
            tt =  self.total_time(piles, mid_k)
            # print(low_k, mid_k, high_k, tt)
            if tt <= h:
                high_k = mid_k
            else:
                low_k = mid_k + 1 
        return high_k
        



