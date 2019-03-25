import math
def bulbSwitch_(n) :
    arr = [False for _ in range(n+1)]
    for i in range(1,n+1) :
        k = 1
        while k*i<=n :
            arr[k*i] = not arr[k*i]
            k+=1
    cnt = 0
    for i in arr :
        if i :
            cnt += 1
    return cnt
def bulbSwitch(n) :
    return int(math.sqrt(n))
if __name__ == '__main__' :
    print(bulbSwitch(3))