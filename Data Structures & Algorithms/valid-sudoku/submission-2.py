class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row_set = set()
            col_set = set()
            for x in range(9):
                #row check
                if board[i][x].isnumeric() and board[i][x] not in row_set:
                    row_set.add(board[i][x])
                elif board[i][x] in row_set:
                    return False
                #col check
                if board[x][i].isnumeric() and board[x][i] not in col_set:
                    col_set.add(board[x][i])
                elif board[x][i] in col_set:
                    return False
        #3x3 check
        for i in range(9):
            if i % 3 == 0:
                tarr1, tarr2, tarr3 = set(), set(), set()
            for x in range(9):
                if x < 3 and board[i][x].isnumeric() and board[i][x] not in tarr1:
                    tarr1.add(board[i][x])
                elif x < 3 and board[i][x] in tarr1:
                    return False
                if 3 < x < 6 and board[i][x].isnumeric() and board[i][x] not in tarr2:
                    tarr2.add(board[i][x])
                elif 3 < x < 6 and board[i][x] in tarr2:
                    return False
                if 6 < x < 9 and board[i][x].isnumeric() and board[i][x] not in tarr3:
                    tarr3.add(board[i][x])
                elif 6 < x < 9 and board[i][x] in tarr3:
                    return False
                
        return True
                