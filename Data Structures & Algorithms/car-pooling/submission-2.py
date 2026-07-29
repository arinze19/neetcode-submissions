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
        # this number line approach does not work becuse 
        # on the line is considered overlapping 
        count = 0
        points = []

        for passengers, start, end in trips: #O(n)
            points.append([start, passengers])
            points.append([end, -passengers])
            

        points.sort()
        for time, passengers in points:
            count += passengers
            if count > capacity:
                return False

        return True 
        # [[1,4][2,-4][2,3][4,-1]] - this works because it is sequential which is fine 




        
