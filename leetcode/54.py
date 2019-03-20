def spiralOrder(matrix):
    if matrix == [] :
        return []
    n = len(matrix)
    m = len(matrix[0])
    step = [[0,1],[1,0],[0,-1],[-1,0]] 
    ret = [[0 for _ in range(m)] for _ in range(n)]
    ans = []
    idx = 1
    d = 0
    i=j=0
    while idx<=n*m :
        ans.append(matrix[i][j])
        ret[i][j] = idx 
        while idx<n*m and (i+step[d][0]>=n or i+step[d][0]<0 or j+step[d][1]>=m or j+step[d][1]<0 or ret[i+step[d][0]][j+step[d][1]]):
            d = (d+1)%4 
        i = i+step[d][0]
        j = j+step[d][1]
        idx += 1
    return ans
if __name__ == '__main__' :
    ans = spiralOrder([])
    print(ans)