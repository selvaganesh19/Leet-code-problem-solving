class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        col , d1 , d2 = set(),set(),set()
        place = []

        def backtrack(row):
            if row == n:
                res.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in place])
            
            for i in range(n):
                if i in col or row - i in d1 or row + i in d2:
                    continue
                
                col.add(i); d1.add(row - i); d2.add(row + i)
                place.append(i)
                backtrack(row+1)
                col.remove(i); d1.remove(row - i); d2.remove(row+i)
                place.pop()
        
        backtrack(0)
        return res

  
