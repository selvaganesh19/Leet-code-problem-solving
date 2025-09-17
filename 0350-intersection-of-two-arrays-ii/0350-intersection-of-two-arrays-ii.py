class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        f={}
        res=[]

        for i in nums1:
            f[i] = f.get(i,0)+1
        

        for i in nums2:
            if i in f and f[i] > 0:
                res.append(i)
                f[i] -=1
        
        return res