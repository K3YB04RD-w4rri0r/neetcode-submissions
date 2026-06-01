class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [i.lower() for i in s if i.isalnum()]
        p1 = 0
        p2 = len(l)-1 
        while p1 < p2:
            if l[p1] != l[p2]:
                return False
            p1 += 1
            p2 -= 1

        return True

                