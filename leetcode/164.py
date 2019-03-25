def maximumGap(nums) :
    nums.sort()
    ret = 0
    for i in range(len(nums)-1) :
        ret = max(ret , nums[i+1]-nums[i])
    return ret
if __name__ == '__main__' :
    print(maximumGap([3,6,9,1]))