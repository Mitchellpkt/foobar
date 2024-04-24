from typing import List, Generator


def doubling(batch_size: int = 3, max_val: int = 1000) -> Generator[List[int], None, None]:
    """
    Example of a batched generator with finite outputs.
    Doubles internal state `i` repeatedly (remembered within/between calls).
    Each call from an outside loop yields a batch of `batch_size` values.
    After max_value is hit, the generator stops.

    :param batch_size: The number of doubled values to yield per batch.
    :param max_val: The maximum value of `i` at which the generator stops.
    :return: Yields lists of integers.
    """

    # Initialized once (not reset between calls!)
    i: int = 1

    # For a given call that doesn't exhaust the generator...
    while i < max_val:

        # Build the batch
        batch_result: List[int] = []  # Collect results in a batch
        while len(batch_result) < batch_size and i < max_val:
            batch_result.append(i)
            i *= 2  # Double the value of i

        yield batch_result  # << Code & state freezes here! (until next call)

# Usage
if __name__ == "__main__":
    for batch in doubling(batch_size=3, max_val=1000):
        print(batch)
