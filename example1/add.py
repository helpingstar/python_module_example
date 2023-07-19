# add.py
"""This is __doc__"""

# __annotations__
v_int: int = 3
v_str: str


def add1(a: int, b: int) -> int:
    return a + b


def add2(a: int, b: int) -> int:
    result = a + b
    return result


def _add3(a: int, b: int) -> int:
    return a + b
