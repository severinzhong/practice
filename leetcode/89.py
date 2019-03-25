def grayCode(n) :
    '''
    my graycode generate function with recur
    '''
    d = [(1<<x) for x in range(n)]
    def find(ret) :
        if len(ret) == 1<<n :
            return ret 
        for i in d :
            if not (ret[-1]^i in ret) :
                ret = find(ret+[ret[-1]^i])
        return ret
    return find([0])
def grayCode_(n):
    """
    offical grayCode generate function O(1<<n)
    """
    res = []
    for i in range(1<<n):
        res.append(i^(i>>1))      
    return res
def grayCode__(n):
    """
    gray code with mirro method
    Such as n = 1 , the gray code is [0,1] ;
    and when n = 2 , the gray code is [0,1,3,2] , equal to [0,1] + [1,0](each element plus 2**(n-1))
    so when n = 3 , the gray code is [0,1,3,2] + [2,3,1,0](each element plus 2**2) , just [0,1,3,2,6,7,5,4]
    """
    if n == 0:
        return [0]
    temp = grayCode(n-1)
    temp1 = [i+2**(n-1) for i in temp[::-1]]
    res = temp + temp1
    return res
if __name__ == '__main__' :
    print(grayCode(4))
