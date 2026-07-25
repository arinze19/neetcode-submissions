nums = [1,2,3,4,5]

def prefix_sum(nums):
    prefix = [0 for _ in range(len(nums) + 1)]
    
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
        
    return prefix
        
print(prefix_sum(nums))