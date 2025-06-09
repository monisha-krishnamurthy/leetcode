class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        store = self.keystore.get(key, []) 
        left, right = 0, len(store)-1

        while left <= right:
            mid = (left+right)//2
            if store[mid][1] <= timestamp:
                res = store[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
