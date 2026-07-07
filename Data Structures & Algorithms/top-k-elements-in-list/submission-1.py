from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Questions 
        1. Answer is always unique
        2. We can return output in any order 
        3. can k be greater than the length of nums? No
        4. is the array sorted? No

        Thought process
        1. create a hash map 
        2. loop through the nums array
        3. keep a frequency count of each item
        4. loop through the hash map and add (frequency, num) into a heap
        5. fetch k items out of the heap

        Time and Space 
        1. Time | O(n) + O(n) + O(klogn)
        2. Space | O(n) + O(n)
        '''
        freq_table = defaultdict(int)
        res = []

        for num in nums: # O(n)
            freq_table[num] += 1

        buckets = [[] for i in range(len(nums) + 1)] # at most len(nums) items

        for num, count in freq_table.items():
            buckets[count].append(num)

        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for j in range(len(bucket)):
                res.append(bucket[j])

                if len(res) == k:
                    return res

        return []

