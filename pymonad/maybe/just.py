from .maybe import Maybe
from .nothing import Nothing

class Just(Maybe):
    ok = True

    def map(self, f):
        a = f(self.value)
        if (isinstance(a, Just) or isinstance(a, Nothing)): return a
        return Just(a)

    def __str__(self):
        return 'Just (%s)' % self.value
