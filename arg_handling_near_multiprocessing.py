from multiprocessing import Pool, cpu_count
from typing import List

if cpu_count == 1:
    print(
        f"FYI: Demoing multiprocessing with only one available core will be slower (but should functionally work)."
    )


def foo_raw(arg0: str, index_1: int = 2, index_2: int = 3) -> str:
    return arg0[index_1] + arg0[index_2]


# WRONG WAY
def handler(example_args: List[str], index_1: int = 2, index_2: int = 3):
    def wrapped_foo(arg0: str) -> str:
        return foo_raw(arg0, index_1=index_1, index_2=index_2)

    with Pool(3) as pool:
        result = pool.map(wrapped_foo, example_args)

    return result


# Right(??) way
def auto_wrapper(funct, args, kwargs):
    ...


if __name__ == "__main__":
    try:
        results = handler(example_args=["ABC", "DEF", "GHI"])
    except AttributeError as e:
        print(
            f"The wrong way raised an AttributeError about pickling, as expected:\n\t{e}"
        )
