# Pymonad

> Exploring monad concepts in Python

## Getting Started

```python
from pymonad import Maybe

# util functions defined out of scope.
def lower(x): return x.lower()
def reverse(x): return x[::-1]
def shout(x): return '%s!' % x
def capitalise(x): return x.capitalize()

# using operator overloads
a = Just('Adam')
b = a >> lower >> reverse >> shout >> capitalise
print(b | "n/a") # print "Mada!" otherwise "n/a" if Nothing.

# using explicit method names
x = Nothing()
y = x.map(lower).map(reverse).map(shout).map(capitalise)
print(y.get()) # defaults to None if not explictly specified.

# determine if Just or Nothing
a.is_just() # True
x.is_nothing() # True

# stringify the instance
print(Just('Imogen')) # Just (Imogen)
print(Nothing()) # Nothing
```
