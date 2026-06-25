# intervals=[(0,50),(10,60),(60,110),(70,120),(20,70),(30,80),(40,90),(50,100),(80,130),(90,140),(100,150)]
intervals = [(0,40),(5,10),(15,20)]
# intervals = [(4,9)]


def meetingRoomTwo(intervals):
    intervals.sort(key=lambda x: x[1])
    
    
    
    print(intervals)
    
    
meetingRoomTwo(intervals)