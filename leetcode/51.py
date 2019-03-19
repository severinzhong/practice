# n queen
def solveNQueens(n):
    M = [['.' for y in range(n)] for x in range(n)]
    ret = []
    def can(M , x ,y) :
            for  i in range(n) :
                    if M[i][y] == 'Q' :
                            return False
                    if M[x][i] == 'Q' :
                            return False
            i = 0
            while x+i<n and y+i<n :
                    if M[x+i][y+i] == 'Q' :
                            return False
                    i += 1
            i = 0
            while x-i>=0 and y-i>=0 :
                    if M[x-i][y-i] == 'Q' :
                            return False
                    i += 1
            i = 0
            while x+i<n and y-i>=0 :
                    if M[x+i][y-i] =='Q' :
                            return False
                    i += 1
            i = 0
            while x-i>=0 and y+i<n :
                    if M[x-i][y+i] =='Q' :
                            return False
                    i += 1
            return True
    def queen( M , cnt) :
            if cnt==n :
                    ans = []
                    for i in range(n) :
                            ans.append(''.join(M[i]))
                    if ans not in ret :
                            ret.append(ans)
            else :
                    for i in range(n) :
                            if can( M , cnt , i) :
                                    M[cnt][i] = 'Q'
                                    #print(M)
                                    queen(M,cnt+1)
                                    M[cnt][i] = '.'
    queen(M , 0)
    return ret
if __name__ == '__main__' :
    print(solveNQueens(4))