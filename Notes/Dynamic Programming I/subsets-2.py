import time

def subsets_two(nums):
    path, res = [], []

    def backtrack(start):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return res

prev = None
for n in range(10, 21, 2):
    nums = list(range(n))
    start = time.perf_counter()
    subsets_two(nums)
    elapsed = time.perf_counter() - start
    ratio = f"{elapsed / prev:.1f}x" if prev else "-"
    print(f"n={n:2d}  {elapsed * 1000:9.2f} ms  vs previous: {ratio}")
    prev = elapsed