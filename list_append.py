from time import perf_counter
from typing import List

n: int = 100_000_000
max_allowed_time_sec: float = 20
last_time_took_sec: float = 0

exponent: int = 7
while last_time_took_sec < max_allowed_time_sec:
    test_list: List[float] = list(range(10**exponent))
    tic: float = perf_counter()
    for i in range(n):
        test_list.append(i)
    toc: float = perf_counter()
    last_time_took_sec = toc - tic
    print(f"10**{exponent} took: {last_time_took_sec:.2f} seconds")
    exponent += 1

# Results
# 10**7 took: 6.33 seconds
# 10**8 took: 6.27 seconds
# 10**9 took: 6.29 seconds
