'''
log(2)太慢了
log(10)走起
'''
def superPow_(a , b) :
    def divide2(b) :
        n = len(b)
        for i in range(n) :
            if b[i]%2 == 1 and i<n-1 :
                b[i+1] += 10
            b[i] = b[i]//2
        while b[0] == 0 and len(b)>1 :
            b = b[1:]
        return b
    ret = 1
    while b!=[0] :
        if b[-1]%2 == 1 :
            ret = ret*a % 1337
        a = a*a%1337
        b = divide2(b)
    return ret
def superPow( a, b):
    if not b:
        return 1
    return pow(a, b.pop(), 1337)*superPow(pow(a, 10, 1337), b)%1337
if __name__ == '__main__' :
    print(superPow(3,[4]))