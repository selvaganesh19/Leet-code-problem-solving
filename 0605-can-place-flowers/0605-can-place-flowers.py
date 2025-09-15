class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        z,a=1,0

        for i in flowerbed:
            if i ==0:
                z+=1
            else:
                a+=(z-1)//2
                z=0
        
        return a+z // 2 >=n