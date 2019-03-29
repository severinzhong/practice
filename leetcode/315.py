class Solution:
    def countSmaller(self,nums) :
        copy = [x for x in nums] 
        nums.sort()
        n = len(nums)
        tsum = [0 for i in range(n+1)]
        def update(i) :
            i += 1
            while i<=n :
                tsum[i] += 1
                i += i&-i
        def sumrange(i) :
            i+=1
            ans = 0
            while i>0 :
                ans += tsum[i]
                i -= i&-i  
            return ans  
        def find(x) :
            l ,r = 0 , n-1
            while l<=r :
                m = (l+r) // 2 
                if nums[m] == x :
                    while m>0 and nums[m-1]==x :
                        m -= 1
                    return m
                elif nums[m]>x :
                    r = m-1
                else :
                    l = m+1
            return -1
        ret = []
        for i in copy :
            idx = find(i)
            # print(i,idx , sumrange(idx-1))
            ret.append(idx-sumrange(idx-1))
            update(idx)
        return ret
    def countSmaller_(self, nums): # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/248045/python-mergeSort-and-binary-index-tree
        ind = {v: i+1 for i, v in enumerate(sorted(set(nums)))}
        m = len(ind)+1
        pre = [0]*m

        def update(i, add=1):
            while i < m:
                pre[i] += add
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += pre[i]
                i -= i & -i
            return s
        ret = []
        for v in reversed(nums):
            i = ind[v]
            ret.append(query(i-1))
            update(i)
        return ret[::-1]
if __name__ == "__main__":
    nums = [3,3,4,2,2,1,1]
    ret = Solution().countSmaller(nums)
    print(ret)