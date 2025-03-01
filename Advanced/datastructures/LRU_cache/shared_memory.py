from multiprocessing import shared_memory
import numpy as np

# Create shared memory
size = 10  # 10 integers
shm = shared_memory.SharedMemory(create=True, size=size * np.int64().nbytes)
array = np.ndarray((size,), dtype=np.int64, buffer=shm.buf)
array[:] = np.arange(size)  # Fill with numbers 0-9

print("Shared Memory Name:", shm.name)

# Attach to shared memory
shm2 = shared_memory.SharedMemory(name=shm.name)
array2 = np.ndarray((size,), dtype=np.int64, buffer=shm2.buf)
print("Read from Shared Memory:", array2[:]) 

# Cleanup (only when done)
shm.close()
shm.unlink()  # Unlinks shared memory (removes it when all processes are done)