from typing import Union


a: int | str = 5
print(a)
a = "abc"
print(a)
a = 8
print(a)
b: Union[int, str] = 5
print(b)
b = "abc"
print(b)
b = 8
print(b)
b= 7.2
