# exec1.py
import add

print(add.add1(2, 3))
# 5
print(add.add2(2, 3))
# 5
print(add.__name__)
# add
print(add.__file__)
# ~~\module_example\example1\add.py
print(add.__annotations__)
# {'v_int': <class 'int'>, 'v_str': <class 'str'>}
print(add.__doc__)
# This is __doc__
