from time import perf_counter

n: int = 10_000_000

# No try/except overhead
tic: float = perf_counter()
for i in range(n):
    assert i == i
toc: float = perf_counter()
print(f"No try/except: {toc - tic:.2f} seconds")

# With try/except overhead
tic: float = perf_counter()
for i in range(n):
    try:
        assert i == i
    except:
        pass
toc: float = perf_counter()
print(f"No try/except: {toc - tic:.2f} seconds")
