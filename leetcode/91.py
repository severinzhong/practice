#decode ways
def numDecodings(s) :
    n = len(s)
    if n==0 :
        return 0
    if s[0]=="0" :
        return 0
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1 
    for i in range(2,n+1) :
        if int(s[i-2:i])<=26 and int(s[i-2:i])>0:
            if s[i-1]=='0' :
                dp[i] = dp[i-2]
            elif s[i-2]=='0' :
                dp[i] = dp[i-1]
            else :
                dp[i] = dp[i-1] + dp[i-2]
        elif s[i-1]== '0':
            return 0
        else :
            dp[i] = dp[i-1]
    return(dp[n])
if __name__ == '__main__' :
    print(numDecodings("101"))