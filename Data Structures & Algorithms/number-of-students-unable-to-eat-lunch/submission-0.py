from collections import deque, Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        '''
        Keywords
        1. 0 - circle | 1 - square
        2. return number of students unable to eat

        Questions 
        1. sandwich and student length are the same 
        2. is it possible to not have an answer? Yes 

        Thought process
        BRUTE FORCE
        0. define variables 
            - count = 0
            - length = len(students)
        1. while length:
        2. for _ in range(length):
        3. compare top student and top sandwich
            - if same, pop from both
            - else move student back to queue
        4. if len(students) == length: # no possible student found 
                return count 
            else:
                length = len(students)

        OPTIMAL
            - count number of students for both kind of sandwiches 
            - while queue
                * if queue[0] in count:
                    queue.popleft()
                    count[queue[0]] -= 1
                  else:
                    return len(queue)
        '''
        queue = deque(sandwiches)
        count = Counter(students)

        while queue:

            if count[queue[0]] > 0:
                top = queue.popleft()
                count[top] -= 1
            else:
                return len(queue)
        
        return 0
