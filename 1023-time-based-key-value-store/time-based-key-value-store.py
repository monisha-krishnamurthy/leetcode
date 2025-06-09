class TimeMap:

    def __init__(self):
        self.keystore = defaultdict(SortedDict)   # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore:
            return ""
        
        timestamps = self.keystore[key]
        idx = self.keystore[key].bisect_right(timestamp) - 1

        if idx >= 0:
            closest_time = timestamps.iloc[idx]
            return timestamps[closest_time]
        return "" 
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
