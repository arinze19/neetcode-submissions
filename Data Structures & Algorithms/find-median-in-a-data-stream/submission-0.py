class MedianFinder:
    # space | O(n)
    def __init__(self):
        self.arr = []

    # time | O(1) + O(nlogn)
    def addNum(self, num: int) -> None:
        self.arr.append(num)

        self.arr.sort()

    # time | O(1)
    def findMedian(self) -> float:
        if len(self.arr) % 2 == 0:
            right = len(self.arr) // 2
            left = right - 1

            return (self.arr[left] + self.arr[right]) / 2
        else:
            mid = len(self.arr) // 2
            return self.arr[mid]
        
        