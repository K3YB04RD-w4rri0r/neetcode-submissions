class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        brute: calculate all distances to x , sort in asc order take first k elts (n + nlogn)
        """

        distances = [(abs(x - e), e) for e in arr]

        distances.sort()

        result = [e for _, e in distances[:k]]

        return sorted(result)
            
