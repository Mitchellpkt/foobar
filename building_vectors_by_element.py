from numpy import array, zeros
from time import perf_counter
from typing import List

N: int = 100_000_000

# Version with list, appending
test_array: List[float] = []
tic: float = perf_counter()
for i in range(N):
    test_array.append(i)
toc: float = perf_counter()
print(f"List append: {toc - tic:.2f} seconds")

# Same as the above, except the list is preallocated
test_array: List[float] = [0] * N
tic: float = perf_counter()
for i in range(N):
    test_array[i] = i
toc: float = perf_counter()
print(f"List preallocated: {toc - tic:.2f} seconds")

# Same except with a numpy array
test_array_np = zeros(N)
tic: float = perf_counter()
for i in range(N):
    test_array_np[i] = i
toc: float = perf_counter()
print(f"Numpy array: {toc - tic:.2f} seconds")

# Results
# List append: 5.78 seconds
# List preallocated: 5.05 seconds
# Numpy array: 10.03 seconds
