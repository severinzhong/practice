class NumArray:

    def __init__(self, nums):
        self.n = len(nums)+1
        self.nums = [0] + nums
        self.tsum = [0] + nums
        i = 2
        while i<=self.n :
            j = i
            while j<self.n :
                self.tsum[j] = self.tsum[j] + self.tsum[j - i//2]
                j += i
            i*=2
        # print(self.tsum)
    def update(self, i, val) :
        i += 1
        add = val - self.nums[i]
        self.nums[i] = val
        while i<self.n :
            self.tsum[i] += add 
            i += (i&-i)
        # print(self.tsum)
    def sumToi(self, i) :
        ret = 0
        i += 1
        while i>0 :
            ret += self.tsum[i]
            i -= i&-i
        return ret
    def sumRange(self, i, j) :
        return self.sumToi(j) - self.sumToi(i) + self.nums[i+1]

if __name__ == "__main__":
    ret = NumArray([1,1,1,1,1])
    print(ret.sumRange(0,3))