class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr) == 1:
            return self.arr[0]
        
        result = 0

        if len(self.arr) % 2 == 0:
            mid = (len(self.arr)//2) -1
            mid_1 = (len(self.arr)//2 + 1) -1
            result = (self.arr[mid] + self.arr[mid_1])/2
        else:
            result = self.arr[len(self.arr)//2]

        return result





# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()