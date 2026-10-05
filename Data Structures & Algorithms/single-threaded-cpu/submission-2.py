import heapq 

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        double ended heap
        Keywords 
        - [enqueueTime, processingTime]
        - shortest_processing_time first
        - smallest_index (index on the tasks order OR enqueueTime)
        Thought Process 
        - sort tasks by time 
        - while curr_time >= queue[0]
            -> add to priority_queue
        - while priority_queue
            -> process based on processing time
            -> update time 
        '''

        heap = []
        heap_2 = []
        count = 0
        res = []

        for i, (enqueue_time, processing_time) in enumerate(tasks):
            heapq.heappush(heap, (enqueue_time, processing_time, i))

        while heap or heap_2:
            # get tasks ready to be processed 
            while heap and heap[0][0] <= count:
                enqueue_time, processing_time, index = heapq.heappop(heap)

                # add to heap_2
                heapq.heappush(heap_2, (processing_time, index))
            
            # process tasks 
            if heap_2:
                processing_time, index = heapq.heappop(heap_2)

                count += processing_time
                res.append(index)
                continue 

            if heap:
                count = heap[0][0] # set to heap enqueue time

        return res


            

