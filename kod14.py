class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.age=age
        self.name=name

    def foo(self) -> None:
        print("Person")


class Student(Person):
    id: int

    def __init__(self, name: str, age: int, id: int) -> None:
        super().__init__(name, age)
        self.id = id

    def foo(self) -> None:
        print("Student")


s1: Student = Student("Nowak",20,123455)
s1.foo()
s2: Person = Student("Nowak",20,123455)
s2.foo()
