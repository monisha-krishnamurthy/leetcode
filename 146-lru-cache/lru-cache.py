from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.dictionary = dict()
        self.queue = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dictionary:
            self.queue.remove(key)
            self.queue.append(key)
            return self.dictionary[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.queue.remove(key)
            self.queue.append(key)
            self.dictionary[key] = value
        else:
            if len(self.queue) < self.capacity:
                self.queue.append(key)
                self.dictionary[key] = value
            else:
                key_to_be_deleted = self.queue.popleft()
                del self.dictionary[key_to_be_deleted]
                self.queue.append(key)
                self.dictionary[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)