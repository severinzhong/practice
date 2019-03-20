# spiral matrix
def generateMatrix(n):
    step = [[0,1],[1,0],[0,-1],[-1,0]] 
    ret = [[0 for _ in range(n)] for _ in range(n)]
    idx = 1
    d = 0
    i=j=0
    while idx<=n*n :
        ret[i][j] = idx 
        while idx<n*n and (i+step[d][0]>=n or i+step[d][0]<0 or j+step[d][1]>=n or j+step[d][1]<0 or ret[i+step[d][0]][j+step[d][1]]):
            d = (d+1)%4 
        i = i+step[d][0]
        j = j+step[d][1]
        idx += 1
    return ret
if __name__ == '__main__' :
    ans = generateMatrix(3)
    for i in ans :
        print(i)