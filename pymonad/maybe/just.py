from .maybe import Maybe
from .nothing import Nothing


class Just(Maybe):
    ok = True

    def map(self, f):
        a = f(self.value)
        if (isinstance(a, Just) or isinstance(a, Nothing)):
            return a
        return Just(a)

    def __str__(self):
        return 'Just (%s)' % self.value

    def __eq__(self, other):
        if (other.ok):
            return Just(self.value == other.value)
        return Nothing()

    def __ne__(self, other):
        if (other.ok):
            return Just(self.value != other.value)
        return Nothing()
