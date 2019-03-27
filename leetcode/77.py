class Solution:
    def combine(self,n,k) :
        if n == 0 :
            return [[]]
        ret = []
        def find(nums , n , k) :
            if len(nums) == k:
                ret.append(nums)
                return
            for i in range(nums[-1]+1,n+1): 
                find(nums + [i] , n , k)
        for i in range(1,n+1):
            find([i] , n , k)
        return ret
if __name__ == "__main__":
    print(Solution().combine(4,2))