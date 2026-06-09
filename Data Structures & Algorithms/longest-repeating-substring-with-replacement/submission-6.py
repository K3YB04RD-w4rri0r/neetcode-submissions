class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        L = 0
        R = 0
        window = {}
        cumsum, maxi = 0, 0
        while R < len(s):
            window[s[R]] = window.get(s[R], 0) + 1
            R += 1
            # print(window)
            if len(window) > 0:
                cumsum = sum(window.values())
                maxi = max(window.values())
            # print(cumsum, maxi)
            # print(cumsum -maxi)
            if not (cumsum - maxi <= k):
                # print("not")
                # print("MAXLEN :", maxlen)
                window[s[L]] -= 1
                L += 1
            maxlen = max(maxlen, R - L)


        maxlen = max(maxlen, R - L - 1)
        # print("MAXLEN" , maxlen)
        return maxlen
        

