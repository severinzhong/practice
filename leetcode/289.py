'''
Game of Life:
Rules:
1.Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2.Any live cell with two or three live neighbors lives on to the next generation.
3.Any live cell with more than three live neighbors dies, as if by over-population..
4.Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
'''
def gameOfLife(board) :
    if board == [] :
        return 
    n = len(board)
    m = len(board[0])
    ret = [[0 for _ in range(m)] for _ in range(n)]
    step = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
    for i in range(n) :
        for j in range(m) :
            cnt = 0
            for s in step :
                if i+s[0]>=0 and i+s[0]<n and j+s[1]>=0 and j+s[1]<m and board[i+s[0]][j+s[1]]==1 :
                    cnt += 1
            if board[i][j] == 1 :
                if cnt < 2 :
                    ret[i][j] = 0
                elif cnt < 4:
                    ret[i][j] = 1
                else :
                    ret[i][j] = 0
            else :
                if cnt == 3 :
                    ret[i][j] = 1
                else :
                    ret[i][j] = 0
    for i in range(n):
        board[i] = ret[i]
if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    gameOfLife(board)
    print(board)
