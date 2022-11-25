from __future__ import  annotations


class Person:
    name: str
    age: int

    def __init__(self, name:str, age: int) ->None:
        self.name = name
        self.age = age

    def __eq__(self, other: object) -> bool:  # type: ignore[override]
        if not isinstance(other, Person):
            return NotImplemented

        return self.name == other.name and self.age == other.age


jack1 = Person('Jack', 23)
jack2 = Person('Jack', 23)
print(jack1 == jack2)
print(jack1 is jack2)