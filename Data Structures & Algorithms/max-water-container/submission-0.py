class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvolume = 0
        p1 = 0
        p2 = len(heights) - 1 
        while p1 < p2:
            print((p2 - p1) * min(heights[p1], heights[p2]))
            maxvolume = max(maxvolume, (p2 - p1) * min(heights[p1], heights[p2]))
            if heights[p1] <= heights[p2]:
                p1 += 1
            else:
                p2 -= 1

        return maxvolume