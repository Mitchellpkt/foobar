from pydantic import BaseModel
from typing import List
from copy import deepcopy


class Foo(BaseModel):
    x: int = None

    def __init__(self, **data):
        super().__init__(**data)
        print("honk " * (self.x + 1))


class Bar(BaseModel):
    y: int
    foos: List[Foo] = None
    nest: bool = True
    recursed_object: object = None

    def __init__(self, **data):
        super().__init__(**data)
        self.foos = [Foo(x=i) for i in range(self.y)]
        self.nest = False
        self.recursed_object = deepcopy(self)


if __name__ == "__main__":
    b: Bar = Bar(y=3)
    print(b)
