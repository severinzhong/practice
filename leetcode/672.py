def flipLights(n,m) :
    if m == 0 or n == 0:
        return 1
    if m == 1 :
        if n == 1 :
            return 2
        if n == 2 :
            return 3
        return 4
    if m == 2 :
        if n == 1 :
            return 2
        if n == 2 :
            return 4
        return 7
    if n== 1 :
        return 2
    if n == 2 :
        return 4
    return 8
if __name__ == '__main__' :
    print(flipLights(2,1))
'''
1 1 2  1 2 2  1 3 2  1 4 2
2 1 3  2 2 4  2 3 4  2 4 4
3 1 4  3 2 7  3 3 8  3 4 8
4 1 4  4 2 7  4 3 8
5 1 4  5 2 7  5 3 8
'''