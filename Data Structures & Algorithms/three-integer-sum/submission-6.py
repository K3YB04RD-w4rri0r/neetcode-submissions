class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st = sorted(nums)
        out = set()
        for b in range(len(st)):
            a, c = 0, len(st) - 1
            while a < b < c:
                if st[a] + st[b] + st[c] < 0:
                    a += 1
                elif st[a] + st[b] + st[c] > 0:
                    c -= 1
                elif st[a] + st[b] + st[c] == 0:
                    out.add((st[a], st[b], st[c]))
                    c -= 1
        
        return [list(i) for i in out]

  