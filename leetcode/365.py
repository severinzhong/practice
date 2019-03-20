#water and jug
# a*x + b*y = z has a solution
# z % gcd(a,b) == 0
def canMeasureWater(x,y,z) :
    if not x or not y or not z:
        return z == 0 or z == x or z == y
    gcd = lambda x, y : x if not y else gcd(y, x % y)
    return x + y >= z and z % gcd(x, y) == 0
if __name__ == '__main__' :
    print(canMeasureWater(1,0,0))