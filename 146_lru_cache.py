class LRUCache:

    def __init__(self, capacity: int):
        self.data = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        # Move current element to the end of the dict
        value = self.data[key]
        del self.data[key]
        self.data[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            # Move to the end updated element
            del self.data[key]
        # If capacity exceeds, we should delete first element from dict
        elif len(self.data) == self.capacity:
            del self.data[next(iter(self.data))]
        # Inserting at the end of map new pair
        self.data[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)