class Solution(object):
    def splitWordsBySeparator(self, w, s):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """

        res = []

        for i in w:
            res.extend(i.split(s))
        
        return [w for w in res if w]