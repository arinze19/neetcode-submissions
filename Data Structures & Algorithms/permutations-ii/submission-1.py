class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # base case
        # if len(path) == len(nums)
        res = []

        nums.sort()

        def backtrack(path, options):
            if len(path)== len(nums):
                res.append(path[:])
                return

            for index, item in enumerate(options):
                if index > 0 and options[index] == options[index - 1]:
                    continue

                # add value
                path.append(item)

                # backtrack
                backtrack(path, options[:index] + options[index + 1:])

                # remove values 
                path.pop()

        backtrack([], nums)

        return res