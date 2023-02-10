from time import perf_counter
from numpy import sign

n: int = 100_000_000
input_number: float = -4.22

# numpy sign
tic: float = perf_counter()
for i in range(n):
    a = abs(input_number)
toc: float = perf_counter()
print(f"sign: {toc - tic:.2f} seconds")

# if/then
tic: float = perf_counter()
for i in range(n):
    a = input_number if input_number > 0 else -input_number
toc: float = perf_counter()
print(f"if/then: {toc - tic:.2f} seconds")


##  Results
# sign: 8.41 seconds
# if/then: 6.43 seconds
