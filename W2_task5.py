# 要求五:在一組陣列中找出兩個數，其加總恰等於給定值。每個數不能被重複使用，且必剛好只有一個解。
# 就是要求四的進階題!

def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            x = nums[i] + nums[j]
            if x == target:
                return [i, j]


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9
