from libc.stdlib cimport malloc, free
from libc.string cimport memset
import mmh3

cdef class MLBF:
    cdef:
        int size, num_hashes
        char* bit_array  # Using C-style memory for efficiency

    def __init__(self, int size, int num_hashes):
        """Initialize MLBF with optimized bit array."""
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = <char*> malloc(size)
        memset(self.bit_array, 0, size)  # Initialize all bits to 0

    cdef inline list _hashes(self, str key):
        """Generate multiple hash values using MurmurHash."""
        return [mmh3.hash(key, seed) % self.size for seed in range(self.num_hashes)]

    def insert(self, list keys):
        """Insert multiple keys related to the same entity."""
        for key in keys:
            for index in self._hashes(key):
                self.bit_array[index] = 1

    def query(self, str key):
        """Check if the key is possibly present."""
        return all(self.bit_array[index] for index in self._hashes(key))

    def __dealloc__(self):
        """Free allocated memory when the object is deleted."""
        free(self.bit_array)