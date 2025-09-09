class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()

        for i in range(9):
            for j in range(9):
                c = board[i][j]

                if c == '.':
                    continue
            
                if (c,'r',i) in seen or (c,'cl',j) in seen or (c,'b',i // 3 , j // 3) in seen:
                    return False
            
                seen.add((c,'r',i))
                seen.add((c,'cl',j))
                seen.add((c,'b',i//3,j//3))
        
        return True