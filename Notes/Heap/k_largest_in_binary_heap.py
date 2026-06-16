import heapq

def k_largest_in_binary_heap(A, k):
    candidates = [(-A[0], 0)]
    res = []
    
    for _ in range(k):
        value, index = heapq.heappop(candidates)
        
        res.append(-value)
        
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(A):
            heapq.heappush(candidates, (-A[left], left))
            
        if right < len(A):
            heapq.heappush(candidates, (-A[right], right))
            
    return res

arr = [561, 314, 401, 28, 156, 359, 271, 11, 3]
print(k_largest_in_binary_heap(arr, 5))