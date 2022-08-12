class Foo:
    def v(self) -> str:
        return "foooo"


class Bar:
    def v(self) -> str:
        return "baaar"


if __name__ == "__main__":

    # Foo before Bar
    class FooBar(Foo, Bar):
        x = 0

    print(f"{FooBar().v()=}")

    # Bar before Foo
    class BarFoo(Bar, Foo):
        x = 0

    print(f"{BarFoo().v()=}")

    # FooBarChild
    class FooBarChild(FooBar):
        def v(self) -> str:
            s: str = super().v()
            s += " <child>"
            return s

    print(f"{FooBarChild().v()=}")
