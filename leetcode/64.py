# minmum path sum
def minPathSum(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[(1<<32)-1 for _ in range(m)] for _ in range(n)]
    dp[0][0] = grid[0][0] 
    for i in range(n):
        for j in range(m) :
            if i>0 :
                dp[i][j] = min(dp[i][j] , dp[i-1][j]+grid[i][j])
            if j>0 :
                dp[i][j] = min(dp[i][j] , dp[i][j-1]+grid[i][j])
    return dp[n-1][m-1]
if __name__ == '__main__' :
    print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
