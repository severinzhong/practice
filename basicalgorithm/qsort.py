def qsort(nums,l,r) :
    if l>=r :
        return 
    i = l
    j = r
    x = nums[i]
    while i<j :
        while i<j and nums[j]>x :
            j -= 1
        if i<j :
            nums[i] = nums[j]
        while i<j and nums[i]<x :
            i += 1
        if i<j :
            nums[j] = nums[i]
    nums[i] = x 
    qsort(nums , l , i-1)
    qsort(nums , i+1 , r)
if __name__ == "__main__":
    nums = [1,3,5,4,2]
    qsort(nums , 0 , len(nums)-1)
    print(nums)