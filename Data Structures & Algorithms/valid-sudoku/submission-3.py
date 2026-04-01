class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict = defaultdict(set)
        coldict = defaultdict(set)
        sqdict = defaultdict(set)

        for i in range(9):
            for n in range(9):
                if board[i][n] == ".":
                    continue
                if board[i][n] in rowdict[i] or board[i][n] in coldict[n] or board[i][n] in sqdict[(i//3, n//3)]:
                    return False
                rowdict[i].add(board[i][n])
                coldict[n].add(board[i][n])
                sqdict[(i//3, n//3)].add(board[i][n])

        return True