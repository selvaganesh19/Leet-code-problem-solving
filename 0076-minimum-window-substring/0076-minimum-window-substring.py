class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(t) > len(s):return ""

        w1, w2 = {}, {}

        for c in t: w1[c] = w1.get(c, 0) + 1

        h, n = 0, len(w1)
        l = 0

        res, resl  = [-1, -1] ,float("inf")

        for r in range(len(s)): 
            w2[s[r]] = w2.get(s[r], 0) + 1

            # Character requirement satisfied
            if s[r] in w1 and w2[s[r]] == w1[s[r]]: 
                h += 1

            while h == n:
                if r - l + 1 < resl:
                    res = [l, r]
                    resl = r - l + 1

                w2[s[l]] -= 1

                if s[l] in w1 and w2[s[l]] < w1[s[l]]:
                    h -= 1

                l += 1

        l, r = res
        return s[l:r+1] if resl != float("inf") else ""

