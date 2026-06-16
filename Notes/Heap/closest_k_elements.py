def k_closest_elements(nums, k, target):
    # right is less than k because we need at least k elements in 
    # a window
    left, right = 0, len(nums) - k # valid window at which we can start
    
    while left < right:
        mid = (right + left) // 2 # this is the mid point between two valid windows
        print(f"left: {left} \nright: {right} \nmid: {mid}")
        if target - nums[mid] > nums[mid + k] - target:
            left = mid + 1
        else:
            right = mid
    return nums[left:left + k]

k_closest_elements([-1,1,1,4,6,8,12], 3, 5)