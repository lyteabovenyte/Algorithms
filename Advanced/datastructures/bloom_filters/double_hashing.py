class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize table with None
        self.prime = self._find_nearest_prime(size - 1)  # Choose a prime smaller than size
    
    def _primary_hash(self, key):
        """First hash function: simple modulo operation"""
        return key % self.size

    def _secondary_hash(self, key):
        """Second hash function: ensures non-zero step size"""
        return self.prime - (key % self.prime)

    def insert(self, key, value):
        """Insert a key-value pair into the hash table using double hashing"""
        index = self._primary_hash(key)
        step_size = self._secondary_hash(key)

        i = 0
        while self.table[(index + i * step_size) % self.size] is not None:
            i += 1
            if i == self.size:  # Table is full
                raise Exception("Hash table is full")

        self.table[(index + i * step_size) % self.size] = (key, value)

    def search(self, key):
        """Search for a key and return the associated value"""
        index = self._primary_hash(key)
        step_size = self._secondary_hash(key)

        i = 0
        while self.table[(index + i * step_size) % self.size] is not None:
            stored_key, stored_value = self.table[(index + i * step_size) % self.size]
            if stored_key == key:
                return stored_value
            i += 1
            if i == self.size:
                return None  # Not found

        return None  # Not found

    def delete(self, key):
        """Delete a key from the hash table"""
        index = self._primary_hash(key)
        step_size = self._secondary_hash(key)

        i = 0
        while self.table[(index + i * step_size) % self.size] is not None:
            stored_key, _ = self.table[(index + i * step_size) % self.size]
            if stored_key == key:
                self.table[(index + i * step_size) % self.size] = None
                return True
            i += 1
            if i == self.size:
                return False

        return False  # Not found

    def _find_nearest_prime(self, num):
        """Find the largest prime number less than num"""
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        while num > 1:
            if is_prime(num):
                return num
            num -= 1
        return 2  # Default prime if none found

# Example Usage
hash_table = DoubleHashingHashTable(11)
hash_table.insert(25, "Data1")
hash_table.insert(36, "Data2")
hash_table.insert(47, "Data3")

print(hash_table.search(25))  # Output: Data1
print(hash_table.search(36))  # Output: Data2
print(hash_table.search(47))  # Output: Data3