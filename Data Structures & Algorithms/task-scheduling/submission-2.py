from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        KEYWORDS 
        1. each CPU cycle allows the completion of a single task
        2. task may be completed in any order 
        3. "identical" tasks must be seperated by n CPU cycles 
            - we want to run as many non-identical tasks as possible 

        QUESTIONS 
        1. task length cannot be zero
        2. n can be 0
        3. can we do only one task in a cycle? Yes 

        THOUGHT PROCESS 
        1. keep count of the number of cycles left for a task to be retaken
        2. keep count of the frequency of each tasks[i]

        - Queue 
        - Heap? help keep accurate count of which task comes next
        --------------------
        [X,X] | n=3

        []
        time = 4
        [(4, 1, X)]

        time = 0

        while heap or queue: # while we have tasks to be processed
            time += 1

            if heap:
                next_valid_time, frequency, char = heapq.heappop(heap) # O(n * log n)

                frequency -= 1

                if frequency:
                    queue.append((time + n, frequency, char))

            while queue and queue[0][0] <= time # while the item in the queue is elgible to be processed #O(n)
                top = queue.popleft() # O(1)
                heapq.heappush(heap, top) # O(n * log n)

        return time

        SPACE AND TIME 
        1. time | O(n * log n) - number of items we can process and then add to the heap + O(n) number of items we can process from the queue
        2. space | O(n) - heap | O(n) - queue
        '''
        queue = deque()
        heap = []
        time = 0
        frequency_table = Counter(tasks)

        for table_char, table_freq in frequency_table.items():
            heapq.heappush(heap, (-table_freq, 0, table_char)) # [(freq, time, char)]

        while heap or queue:
            time += 1

            if heap:
                freq, next_valid_time, char = heapq.heappop(heap)

                freq += 1

                if freq != 0:
                    queue.append((freq, time + n, char))

            while queue and queue[0][1] <= time:
                # pull from queue and add to heap
                top = queue.popleft()

                heapq.heappush(heap, top)
        
        return time