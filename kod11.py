class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.age=age
        self.name=name


p1: Person = Person("Kowalski",34)
print(p1.name)