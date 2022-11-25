from __future__ import annotations
from typing import Callable, ClassVar


class A:
    foo: Callable[[int], None]
    bar: ClassVar[Callable[[A, int], None]]
    bad: Callable[[A], None]


A().foo(42)  # OK
A().bar(42)  # OK
# A().bad()  # Error: Too few arguments