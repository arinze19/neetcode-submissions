def subarray_sum(nums, k):
    hash_set = {0: 1}
    prefix_sum = 0
    count = 0
    
    for curr in nums:
        prefix_sum += curr
        target = prefix_sum - k
        
        if target in hash_set:
            count += hash_set[target]
            
        hash_set[prefix_sum] = hash_set.get(prefix_sum, 0) + 1
        
    return count

arr = [-1,-1,2,2]
print(subarray_sum(arr, 2))
