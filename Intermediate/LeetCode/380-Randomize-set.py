class RandomizedSet:

    def __init__(self):
        self._data = []

    def insert(self, val: int) -> bool:
        if val in self._data:
            return False
        else:
            self._data.append(val)

    def remove(self, val: int) -> bool:
        if val in self._data:
            self._data.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        import random
        r = random.randint(0, len(self._data) - 1)
        return self._data[r]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()