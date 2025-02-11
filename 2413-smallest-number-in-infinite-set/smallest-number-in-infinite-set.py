import heapq

class SmallestInfiniteSet:

    def __init__(self):
      self.positiveIntegers = set()
      self.heap = []
      for i in range(1, 1001):
        self.positiveIntegers.add(i)
        heapq.heappush(self.heap, i) 
    
    def popSmallest(self) -> int:
        result = heapq.heappop(self.heap)
        self.positiveIntegers.remove(result)
        return result

    def addBack(self, num: int) -> None:
        if num not in self.positiveIntegers:
            self.positiveIntegers.add(num)
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)