def twoSum(nums, target):
    Dict={}
    for i in range(len(nums)) :
        if nums[i] in Dict:return [Dict[nums[i]],i]
        Dict[target-nums[i]] = i
if __name__ == '__main__' :
    nums = [2,7,11,15]
    print(twoSum(nums,9))