class Solution:
    def maxArea_(self, height) : # simple thought , TLE
        n = len(height)
        ret = 0
        for i in range(n) :
            for j in range(i) :
                ret = max(ret  , min(height[i],height[j])*(i-j))
        return ret  
    def maxArea(self , height) :
        n = len(height)
        ret = 0
        l = 0
        r = n-1
        while l<r :
            ret =max(ret , min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l += 1
            else :
                r -= 1
        return ret    
if __name__ == "__main__":
    height = [1,2]
    ret = Solution().maxArea(height)
    print(ret)