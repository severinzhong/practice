def numSquares(n) :
    import math
    arr = [n+1 for _ in range(n+1)]
    i = 1
    while i**2<=n :
        arr[i**2] = 1
        i += 1
    def find(m) :
        if arr[m]<n+1 :
            return arr[m]
        k = max(int(math.sqrt(m))//2 , 1 )
        while k**2<m :
            if 1+find(m-k**2)<arr[m] :
                arr[m] = 1+find(m-k**2)
            k += 1
        return arr[m]
    find(n)
    return arr[n]
if __name__ == '__main__' :
    for i in range(1,51):
        print(i,numSquares(i))