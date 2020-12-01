from .either import Either
from .left import Left

class Right(Either):
    ok = True

    def map(self, f):
        a = f(self.value)
        if (isinstance(a, Right) or isinstance(a, Left)): return a
        return Right(a)



    def __str__(self):
        return 'Right (%s)' % self.value
