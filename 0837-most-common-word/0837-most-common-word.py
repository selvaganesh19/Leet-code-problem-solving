import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        words = re.findall(r'\w+', paragraph.lower())

        banned_set = set(banned)
        
        freq = {}
        
        for w in words:
            if w not in banned_set:
                freq[w] = freq.get(w, 0) + 1
        
        return max(freq, key=freq.get)