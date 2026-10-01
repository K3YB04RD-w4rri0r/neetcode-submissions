class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tocheck = ""
        perm = ''.join(sorted(s1))
        for i in range(len(s2)- len(s1) + 1):
            tocheck = s2[i:i + len(s1)]
            sortd = ''.join(sorted(tocheck))

            if sortd == perm:
                return True

        return False
