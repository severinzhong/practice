def twoSum(nums, target) :
    n = len(nums)
    for i in range(n):
        l = i + 1
        r = n - 1
        m = (l+r) // 2
        while l<r and nums[m] != target - nums[i]:
            if nums[m] > target - nums[i] :
                r = m - 1
            else :
                l = m + 1
            m = (l + r) // 2
        if nums[m] == target - nums[i] :
            return [i+1 , m+1]
    return
if __name__ == '__main__' :
    print(twoSum([2,7,11,15],9)) 