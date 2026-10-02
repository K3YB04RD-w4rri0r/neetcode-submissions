class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        st = sorted(nums)
        out = set()
        for b in range(len(st)):
            for c in range(b+1, len(st)):
                a, d = 0, len(st) - 1
                while a < b < c < d:
                    if st[a] + st[b] + st[c] + st[d] < target :
                        a += 1
                    elif st[a] + st[b] + st[c] + st[d]> target:
                        d -= 1
                    elif st[a] + st[b] + st[c] + st[d] == target:
                        out.add((st[a], st[b], st[c], st[d]))
                        d -= 1
        
        return [list(i) for i in out]

  