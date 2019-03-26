def setZeroes(matrix) :
    if matrix == [] :
        return
    n = len(matrix)
    m = len(matrix[0])
    zn = [False for _ in range(n)]
    zm = [False for _ in range(m)]
    for i in range(n) :
        for j in range(m) :
            if matrix[i][j] == 0 :
                zn[i] = True
                zm[j] = True
    for i in range(n) :
        for j in range(m) :
            if zn[i] or zm[j] :
                matrix[i][j] = 0 

if __name__ == '__main__' :
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    setZeroes(matrix)
    print(matrix)