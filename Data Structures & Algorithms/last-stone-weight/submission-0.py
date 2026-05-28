import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we have at only one stone 
        if len(stones) == 1:
            return stones[0]

        clone = [-stones[i] for i in range(len(stones))]

        heapq.heapify(clone) # heapify stones

        # while stone 
        while len(clone) > 1:
            first = heapq.heappop(clone)
            second = heapq.heappop(clone)

            diff = (-first) - (-second)

            heapq.heappush(clone, -diff)


        return -clone[0]



