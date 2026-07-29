import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        KEYWORDS
        1. Drives east 
        2. [num_of_passenger, from, to]

        QUESTIONS 
        1. Moving only east, increasing order (sorted) [Interval]
        2. passengers should not pass the capacity given 
        3. the bus capacity can exceed capacity in the bus/trip

        THOUGHT PROCESS
        1. Stack [not work]
            while stack[-1][2] > vehicle[1]
                stack[-1][0] += vehicle[0]
                stack[-1][2] = max(vehicle[2], stack[-1][2])

            if stack[-1][0] > capacity:
                return False

            return True
        2. Heap
            store current number of passengers
            (to, count_of_passengers)
            4 - (2,1)
            while incoming start is greater than end, pop from heap and reduce count 
            add to count and add to heap

            --------------------------
            count = 0 | heap = []
            count = 4 | heap = [(2,4)]
            while from_ > heap[0][0] # while incoming greater than heap top (logn)
                trip_end, passenger_count = heapq.heappop(heap)
                count -= passenger_count
            
            count += incoming_count

            if count > capacity:
                return False
        3. Sweep Line

        TIME AND SPACE 
        1. Space | O(n)
        2. Time | O(n * logn) + O(n * logn)
        '''
        heap = []
        count = 0

        trips.sort(key=lambda x: x[1]) # O(n log n)

        for i in range(len(trips)): # O(n)
            capacity_, from_, to_ = trips[i] # unpack elements

            while heap and from_ >= heap[0][0]: # O(logn) - do we need while/if
                trip_end, passenger_count = heapq.heappop(heap)
                count -= passenger_count

            count += capacity_
            heapq.heappush(heap, (to_, capacity_))

            if count > capacity:
                return False 

        return True 

        '''
        count = 4, [(2, 4)]
        count = 3, [(4, 3)]
        -----------
        count = 2, [(3, 2)]
        count = 
        '''




        
