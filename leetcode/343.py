#interger break
def integerBreak(n) :
    dp = [1 for _ in range(n+1)]
    dp[0] = 0
    for i in range(1,n+1) :
        for j in range(1,i) :
            dp[i] = max(dp[i] , j * (i-j))
            dp[i] = max(dp[i] , dp[j]*(i-j))
    return dp[n]
if __name__ == '__main__' :
    print(integerBreak(10))
