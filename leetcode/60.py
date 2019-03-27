class Solution:
    def getPermutation(self, n, k) :
        p = 1
        k = k-1
        for i in range(1,n) :
            p *= i 
        #print(p)
        d = [i for i in range(1,n+1)]
        ret = []
        t = n-1
        while t>0 :
            #print(d , ret , k , p)
            idx = k//p 
            ret.append(d[idx])
            d = d[:idx] + d[idx+1:]
            k = k%p
            p = p//t 
            t -= 1
        ret.append(d[0])
        return ''.join([str(x) for x in ret])
if __name__ == "__main__":
    for i in range(1,7) :
        print(Solution().getPermutation(3,i))