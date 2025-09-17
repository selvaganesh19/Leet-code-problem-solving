class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """

        w = title.split()

        res = []

        for i in w:
            if len(i) >= 3:
                res.append(i.capitalize())
            else:
                res.append(i.lower())
        
        return " ".join(res)
            