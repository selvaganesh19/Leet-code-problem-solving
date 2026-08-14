class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = {}
        left = best = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            while window[s[right]] > 2:
                window[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best