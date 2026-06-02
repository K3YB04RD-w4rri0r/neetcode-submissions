class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n  ={}
        for i in nums:
            n.setdefault(i, []).append(i)

        # now need to retrieve the k longest 
        l = sorted(n.values(), key = len, reverse = True)

        top_k = [l[i][0] for i in range(k)]
        
        return top_k
        


        