# exec1.py
import sys
import funcs

print(dir(funcs))
# [... 'func1', 'func2', 'var_real']
print(dir(sys))
# ['__breakpointhook__', '__displayhook__', '__doc__', ...]
funcs_exec = 1
print(dir())
# [..., 'funcs', 'funcs_exec', 'sys']
