class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        f={}

        for i in nums:
            f[i] = f.get(i,0)+1
        
        # print(f)

        for i, v in f.items():
            if v >1:
                return True
        return False    