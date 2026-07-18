class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set) # key = (r/3,c/3)

        for r in range (9):
            for c in range (9):
                if board[r][c] ==  ".":
                    continue
                if (
                    board [r][c] in rows[r] or 
                    board [r][c] in cols[c] or 
                    board [r][c] in square[(r // 3,c // 3)]
                    ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True
                    
'''        #for i in range (len(board)):
        #    print(board[i])
        
        # Checking Each Row for duplicates, return False ASAF

        
        for i in range(len(board)):         # 9 iterations    
            if len(board[i]) != 9:
                print("Length Issue")
                #return False
            else:
                # Check Line 1 w.r.t index i
                for j in range(i+1,9):
                    print(board[i][i], board[i][j])
                    if board[i][i] == board[i][j]: # and board[i][i] != "." and board[i][j] != ".":
                        print("DUPLICATE", board[i][i], board[i][j])
                        #return False
                
                    

        # While checking a row for an index, check that index's column for the same number, return false ASAF

        # Checking 3x3 boxes = ??
        '''