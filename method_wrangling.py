# pip install pydantic
from typing import Any

from pydantic import BaseModel


class Foo(BaseModel):
    method_string: str
    bar_method: Any = None
    self_replacing_method: Any = None

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)

        # Match the appropriate method to `bar_method`
        self.bar_method = getattr(self, self.method_string)

        # Set self_replacing to the original function
        self.self_replacing_method = self.self_replacing_method_original

        ## (the above line is similar to the following)
        # if self.method_string == "cube":
        #     self.bar_method = self.cube
        # elif self.method_string == "square":
        #     self.bar_method = self.square
        # else:
        #     raise ValueError

    def square(self, x):
        return x * x

    def cube(self, x):
        return x * x * x

    def self_replacing_method_original(self, x):
        print(f"Self replacing function called with {x}")
        self.self_replacing_method = self.cube
        return x * x * x * x


if __name__ == "__main__":
    print("---------------------------")
    foo = Foo(method_string="square")
    print(foo.bar_method(2))
    goo = Foo(method_string="cube")
    print(goo.bar_method(2))

    print("---------------------------")
    first_call = goo.self_replacing_method(3)
    print(f"{first_call=}")
    second_call = goo.self_replacing_method(3)
    print(f"{second_call=}")
