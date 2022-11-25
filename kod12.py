from typing import ClassVar

class A:
    x: ClassVar[int] = 0  # Class variable only

A.x += 2  # OK

a = A()
a.x = 1  # Error: Cannot assign to class variable "x" via instance
print(a.x)  # OK -- can be read through an instance