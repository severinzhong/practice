#sudoku solver
def solveSudoku(board):
    def isvalid(i,j,board) :
        for k in range(9) : 
            if k!=i and board[k][j]!='.' and board[k][j]==board[i][j] :
                return False
            if k!=j and board[i][k]!='.' and board[i][k]==board[i][j] :
                return False
        x = 3*(i//3)
        y = 3*(j//3)
        for ii in range(3):
            for jj in range(3) :
                if (not (ii+x==i and jj+y==j)) and board[ii+x][jj+y]!='.' and board[ii+x][jj+y] == board[i][j] :
                    return False
        return True
    def solve(board) :
        for i in range(9) :
            for j in range(9) :
                if board[i][j] == '.' :
                    for k in range(1,10):
                        board[i][j] = str(k)
                        if isvalid(i,j,board) and solve(board):
                            return True
                        board[i][j] = '.'
                    return False
        return True
    solve(board)
if __name__ == '__main__' :
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solveSudoku(board)
    for i in board :
        print(i)