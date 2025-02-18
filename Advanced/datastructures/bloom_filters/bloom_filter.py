import mmh3  # MurmurHash for better hashing
import bitarray  # Efficient bit storage
import math

class BloomFilter:
    def __init__(self, size, num_hashes):
        """
        Initialize a Bloom Filter.
        
        :param size: Number of bits in the bit array
        :param num_hashes: Number of hash functions
        """
        self.size = size
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
        return (byte_index, bit_offset)


    def read_bit(self, index):
        element, bit = self.find_bit_coordinates(self.bit_array, index)
        return (self.bit_array[element])
    

    def _hashes(self, item):
        """
        Generate 'num_hashes' hash values using double hashing.
        
        :param item: The input item to be hashed
        :return: A list of hash values
        """
        hash1 = mmh3.hash(item, 42) % self.size  # First hash function (seed=42)
        hash2 = mmh3.hash(item, 84) % self.size  # Second hash function (seed=84)
        # it returns the indices which should switch to 1(bit).
        return [(hash1 + i * hash2) % self.size for i in range(self.num_hashes)]

    def insert(self, item):
        """
        Insert an element into the Bloom Filter.
        
        :param item: The input element to insert
        """
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1  # Set corresponding bits to 1

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
    

# # Example Usage
# bloom = BloomFilter(size=1000, num_hashes=5)

# # Insert elements
# bloom.insert("apple")
# bloom.insert("banana")
# bloom.insert("cherry")

# # Check elements
# print(bloom.check("apple"))  # Output: True (definitely present)
# print(bloom.check("banana"))  # Output: True (definitely present)
# print(bloom.check("grape"))  # Output: False (definitely absent)
# print(bloom.check("orange"))  # Output: True/False (possibly present or definitely absent)