class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        box =[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
               
                num = board[i][j]

                box1 = (i//3)*3 + (j//3)

                if num == ".":
                    continue
                
                if num in r[i]:
                    return False
                
                if num in c[j]:
                    return False
                
                if num in box[box1]:
                    return False
                
                r[i].add(num)
                c[j].add(num)
                box[box1].add(num)

        return True