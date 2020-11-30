# Pymonad

> Exploring monad concepts in Python

## Getting Started

```python
from pymonad import Maybe

# util functions defined out of scope.
lower = lambda x: x.lower()
reverse = lambda x: x[::-1]
shout = lambda x: '%s!' % x
capitalise = lambda x: x.capitalize()

# using operator overloads
a = Maybe('Adam')
b = a >> lower >> reverse >> shout >> capitalise
print(b | "n/a") # print "Mada!" otherwise "n/a" if Nothing.

# using explicit method names
x = Maybe(None)
y = x.map(lower).map(reverse).map(shout).map(capitalise)
print(y.get()) # defaults to None if not explictly specified.

# determine if Just or Nothing
a.is_just() # True
x.is_none() # True

# stringify the instance
print(Maybe('Imogen')) # Just (Imogen)
print(Maybe(None)) # Nothing
```
