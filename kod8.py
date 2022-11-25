def foo(a: int = None) -> None:
    if a is not None:
        print(a+2)


foo(4)
foo()