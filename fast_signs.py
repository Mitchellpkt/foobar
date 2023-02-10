from time import perf_counter
from numpy import sign

n: int = 10_000_000
input_number: float = -4.22

# numpy sign
tic: float = perf_counter()
for i in range(n):
    a = sign(input_number)
toc: float = perf_counter()
print(f"sign: {toc - tic:.2f} seconds")

# if/then
tic: float = perf_counter()
for i in range(n):
    a = 1 if input_number > 0 else -1
toc: float = perf_counter()
print(f"if/then: {toc - tic:.2f} seconds")

# if/then 3 way
tic: float = perf_counter()
for i in range(n):
    a = 1 if input_number > 0 else -1 if input_number < 0 else 0
toc: float = perf_counter()
print(f"if/then 3 way: {toc - tic:.2f} seconds")

##  Results
# sign: 7.19 seconds
# if/then: 0.57 seconds
# if/then 3 way: 0.73 seconds
