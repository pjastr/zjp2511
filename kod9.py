class A:
    x: int

    def __init__(self, x: int) -> None:
        self.x = x  # Aha, attribute 'x' of type 'int'

a = A(1)
a.x = 2  # OK!
# a.y = 3  # Error: "A" has no attribute "y"