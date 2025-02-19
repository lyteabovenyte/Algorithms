import mmh3  # MurmurHash to use alongside fnv-1 hashing to be collision-free.
import bitarray  # Efficient bit storage
import math
import random

"""
    Initialization notes:
    the number of bits to be used in bloom-filter to tolerate the
    max probility of false positives and the number of hash_functions
    to be generated to find the indices of a ceratin key
    could be computed up front using the formula.
    number_of_bits m = -n * ln(p) / ln(2)2 -> p is max_tolerance, is is the max_size
    number_of_hashes k = m/n * ln(2)
"""
class BloomFilter:
    def __init__(self, size, num_hashes, seed=random.randint()):
        """
        Initialize a Bloom Filter.
        taking a seed to generate deterministic hash functions.
        taking the size of buffer and the number of hash_functions
        to determine the indexes of any key in buffer.
        """
        self.size = size
        self.seed = seed
        self.num_hashes = num_hashes
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)  # Initialize all bits to 0

    def find_bit_coordinates(self, index):
        """
            Method find_bit_coordinates is a utility method that,
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
    
    def key_to_positions(self, key):
        """
            Method key_to_positions takes and array of hash functions as
            input, together with a seed to initialize these hash functions
            and the key to be hashed. 
            It returns the set of bits indices that
            needs to be updated in the bloom-filter to read/write key.
        """
        # returing self.num_hashes indices based on self.num_hashes different
        # deterministic hash_functions.
        return [index for index in self._hashes(key)]

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
        def hash_functions(key, i):
            # returns the corresponding index in buffer.
            return (mmh3.hash(str(key), self.seed) + i * self.fnv1_hash(key)) % self.size
        
        # returning self.num_hashes hash_funcitons based on double hashing strategy
        # for the given string key
        return [lambda key, i=i: hash_functions(key, i) for i in range(self.num_hashes)]

    def contain(self, key, positions=None):
        """
        Check if an element is possibly in the Bloom Filter.
        also we can use self.read_bit method here.
        """
        if positions == None:
            positions = self.key_to_positions(key)
        return all(self.bit_array[index] for index in self._hashes(key))

    def insert(self, key):
        """
            Method insert computes the corresponding bit for the key
            using hash_functions and write 1 in those indices.
            is also changes the size of the buffer in respect to 
            the elements that are added to bloom_filter.
            returns buffer after adding key.
        """
        positions = self.key_to_positions(key)
        if not self.contain(key, positions):
            self.size += 1
            for index in positions:
                self.bit_array = self.write_bit(index)
        return self.bit_array

    def false_positive_probibility(self):
        """
            Method false_positive_probibility estimates the probibility of getting
            false positive based on the current status of the filter,
            that is the number of elements currently stored compared to the max capacity
        """
        return math.pow((1 - pow(math.e, self.num_hashes * self.size / len(self.bit_array))), self.num_hashes)

    def __str__(self):
        """
        Return a string representation of the Bloom Filter.
        """
        return self.bit_array.to01()  # Convert bit array to string for visualization