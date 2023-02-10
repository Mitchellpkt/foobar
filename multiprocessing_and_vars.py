from multiprocessing import Pool
from time import sleep
from typing import Dict

touched_bit_rev: Dict[int, str] = {0: "initializing..."}


def increment_print_sleep(process_label: str, num_times: int = 5):
    for _ in range(num_times):
        i = max(touched_bit_rev.keys())
        touched_bit_rev[i + 1] = f"this element last touched by process {process_label}"
        print(f"process {process_label} incremented up to {i + 1}")
        sleep(1)
    print(f"... within process '{process_label}', ended at: {touched_bit_rev}")


with Pool(5) as pool:
    results = pool.map(increment_print_sleep, "abcdefg")

print(f"Global {touched_bit_rev=}")
