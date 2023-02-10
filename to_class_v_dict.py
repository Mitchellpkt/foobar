from pydantic import BaseModel
from time import perf_counter


class Foo(BaseModel):
    x: int = None


class Bar(BaseModel):
    y: int

    def to_foo_class(self):
        return Foo(x=self.y)

    def to_foo_dict(self):
        return {"x": self.y}


if __name__ == "__main__":
    sample_size: int = 10_000_000

    # Benchmark the to_foo_class method versus the to_foo_dict method
    b: Bar = Bar(y=1)

    tic_class: float = perf_counter()
    for i in range(sample_size):
        b.to_foo_class()
    toc_class: float = perf_counter()
    print(f"Class took: {toc_class - tic_class:.2f} seconds")

    tic_dict: float = perf_counter()
    for i in range(sample_size):
        b.to_foo_dict()
    toc_dict: float = perf_counter()
    print(f"Dict took: {toc_dict - tic_dict:.2f} seconds")

# Results:
# Class took: 17.06 seconds
# Dict took: 1.15 seconds
