        if matrix == [] :
            return 0
        n = len(matrix)
        m = len(matrix[0])
        ret = 0
        row = [[0 for _ in range(m) ] for _ in range(n)]
        column = [[0 for _ in range(m) ] for _ in range(n)]
        for i in range(n) :
            for j in range(m) :
                if matrix[i][j] == '0' :
                    row[i][j] = 0
                    column[i][j] = 0
                if matrix[i][j] == '1' :
                    if j>0 :
                        row[i][j] = row[i][j-1]+1
                    else :
                        row[i][j] = 1
                    if i>0 :
                        column[i][j] = column[i-1][j]+1
                    else :
                        column[i][j] = 1
                ret = max(ret , column[i][j])
                ret = max(ret , row[i][j])
        for i in range(1,n) :
            for j in range(1,m) :
                r = row[i][j] 
                for k in range(column[i][j]) :
                    r = min(r , row[i-k][j])
                    ret = max(ret , (k+1)*(r))
        return ret