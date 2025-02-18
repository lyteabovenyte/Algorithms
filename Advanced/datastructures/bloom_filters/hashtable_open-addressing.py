class HashTableOpenAddressing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  # Empty slots
        self.deleted = object()  # Marker for deleted elements

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None and self.table[index] != self.deleted:
            index = (index + 1) % self.size  # Linear probing
            if index == original_index:  # Table is full
                raise Exception("Hash table is full!")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break  # Full loop, key not found
        return None

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index][0] == key:
                self.table[index] = self.deleted  # Mark slot as deleted
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break  # Full loop, key not found
        return False

    def display(self):
        for i, slot in enumerate(self.table):
            print(f"Index {i}: {slot}")

# Example usage
ht = HashTableOpenAddressing()
ht.insert(15, "A")
ht.insert(25, "B")
ht.insert(35, "C")  # Collision at index 5
ht.insert(10, "D")
ht.display()
print("Search 25:", ht.search(25))
ht.delete(25)
ht.display()