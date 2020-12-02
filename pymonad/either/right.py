from . import Either, Left


class Right(Either):
    ok = True

    def map(self, f):
        a = f(self.value)
        if (isinstance(a, Right) or isinstance(a, Left)):
            return a
        return Right(a)

    def __str__(self):
        return 'Right (%s)' % self.value

    def __eq__(self, other):
        if (other.ok):
            return Right(self.value == other.value)
        return Left(self.value)

    def __ne__(self, other):
        if (other.ok):
            return Right(self.value != other.value)
        return Left(self.value)
