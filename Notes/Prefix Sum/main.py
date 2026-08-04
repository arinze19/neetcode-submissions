nums = [1,2,3,4,5]

def prefix_sum(nums):
    prefix = [0 for _ in range(len(nums) + 1)]
    
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
        
    return prefix

def prefix_sum_alt(nums):
    prefix = [0] * len(nums)
    
    prefix[0] = nums[0]
    
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]
        
    return prefix
        
print(prefix_sum(nums))