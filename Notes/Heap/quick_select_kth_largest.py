import random

def quick_select_k_largest(arr, k):
    def partition(left, right):
        pivot = arr[right]
        j = left - 1
        
        for i in range(left, right):
            if arr[i] <= pivot:
                j += 1
                arr[j], arr[i] = arr[i], arr[j]
        j += 1
        arr[right], arr[j] = arr[j], arr[right]
            
        return j
    
        
    def select(left, right):
        while left <= right:
            index = len(arr) - k
            
            pivot = partition(left, right)
            
            if pivot == index:
                return arr[pivot]
            elif pivot < index:
                left = pivot + 1
            else:
                right = pivot - 1
                
        return -1
    
    return select(0, len(arr) - 1)
    
arr = [8, 2]
k = 2

print(quick_select_k_largest(arr, k))