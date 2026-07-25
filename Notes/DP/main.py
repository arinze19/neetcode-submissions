def stairs(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp)
    return dp[n]


def optimal_fall(grid):
  
    directions = [(-1,-1),(-1,0),(-1,1)]
    
    for row in range(1, len(grid)):
        for col in range(len(grid)):
            current_max = 0
            
            for left, right in directions:
                dr = left + row 
                dc = right + col
                
                if 0 <= dc < len(grid):
                    current_max = grid[row][col] + grid[dr][dc]
                    
            grid[row][col] = current_max
            
    return max(grid[-1])
                

# stairs(5)
grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(optimal_fall(grid))