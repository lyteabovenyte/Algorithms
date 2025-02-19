import mmh3  # MurmurHash for better hashing
import bitarray  # Efficient bit storage
import math

class BloomFilter:
    def __init__(self, size, num_hashes, seed):
        """
        Initialize a Bloom Filter.
        
        :param size: Number of bits in the bit array
        :param num_hashes: Number of hash functions
        """
        self.size = size
        self.seed = seed
        self.num_hashes = num_hashes
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)  # Initialize all bits to 0

    def find_bit_coordinates(self, index):
        """
            function find_bit_coordinates is a utility method that,
            given the index of a bit in a bit-array returns the
            index of the array and the offset of the bit with
            repect to the array's element at that index.
        """
        # since we are using bitarray module.
        BITS_PER_INT = 8
        byte_index = math.floor(index // BITS_PER_INT)
        bit_offset = index % BITS_PER_INT
        return (self.bit_array[byte_index], bit_offset)

    def read_bit(self, index):
        """
            Method read_bit extracts the index-th bit from
            bit_array passed as first argument.
            it returns the value of the bit, so either 0 or 1.
        """
        element, bit = self.find_bit_coordinates(self.bit_array, index)
        return (self.bit_array[element] & (1 << bit)) >> bit
    
    def write_bit(self, index):
        """
            Method write_bit change the index-th bit to 1.
            this version of bloom_filter doesn't support deleting
            so we just wirte 1 at the corresponding index.
        """
        element, bit = self.find_bit_coordinates(index)
        self.bit_array[element] = self.bit_array[element] | (1 << bit)
        return self.bit_array
    
    def key_to_positions(self, hash_functions, key):
        """
            Method key_to_positions takes and array of hash functions as
            input, together with a seed to initialize these hash functions
            and the key to be hashed. 
            It returns the set of bits indices that
            needs to be updated in the bloom-filter to read/write key.
        """
        hM = mmh3.hash(key, self.seed)
        hF = self.fnv1_hash(key)
        # returing self.num_hashes indices based on self.num_hashes different
        # deterministic hash_functions.
        return [self._hashes[i](key) for i in range(self.num_hashes)]

    def fnv1_hash(self, key):
        """ Computing FNV-1 64-bit hash."""
        h = 14695981039346656037  # FNV-1 64-bit offset basis
        fnv_prime = 1099511628211
        for byte in key.encode():
            h ^= byte
            h *= fnv_prime
        return h
        
    def _hashes(self, key):
        """
            Method _hashed uses self.size (number of bits held by bloom_filter)
            and the number of desired hash_functions (self.num_hashes)
            and creates and returns a list of double hashing funcitons,
            taking two values and returning their hash.
        """
        def hash_functions(key):
            return (mmh3.hash(str(key), self.seed) + i * self.fnv1_hash(key) for i in range(self.num_hashes)) % self.size
        
        # returning self.num_hashes hash_funcitons based on double hashing strategy
        # for the given string key
        return [lambda key, i=i: hash_functions(key, i) for i in range(self.num_hashes)]

    def contain(self, item):
        """
        Check if an element is possibly in the Bloom Filter.
        
        :param item: The input element to check
        :return: True if possibly present, False if definitely absent
        """
        return all(self.bit_array[hash_val] for hash_val in self._hashes(item))

    def __str__(self):
        """
        Return a string representation of the Bloom Filter.
        """
        return self.bit_array.to01()  # Convert bit array to string for visualization