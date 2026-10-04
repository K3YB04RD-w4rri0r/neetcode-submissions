class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """ bruteforce
        count = 0
        for l in range(len(nums)):
            for r in range(l, len(nums)):
                if prefix[r+1] == k + - prefix[l]:
                    count += 1
        """
        prefix = [0]
        s = 0
        for i in nums:
            s += i
            prefix.append(s)

        # print(prefix)
        seen = {0: 1}
        count = 0

        for i in range(len(nums)):
            current = prefix[i + 1]
            needed = current - k

            if needed in seen:
                count += seen[needed]

            seen[current] = seen.get(current, 0) + 1

        return count