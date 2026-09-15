class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        mp = {c:[] for c in range (numCourses)}

        for crs,pre in prerequisites:
            mp[crs].append(pre)
        
        res=[]
        cycle,visit= set(),set()

        def dfs(crs):

            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)

            for pre in mp[crs]:
                if not dfs(pre):
                    return []
            
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res