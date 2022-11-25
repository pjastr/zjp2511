from typing import Optional


# Use Optional[X] for a value that could be None
# Optional[X] is the same as X | None or Union[X, None]
x: str = "something" if 3>4 else None
# Mypy understands a value can't be None in an if-statement
if x is not None:
    print(x.upper())
# If a value can never be None due to some invariants, use an assert
assert x is not None
print(x.upper())