from . import Either


class Left(Either):
    ok = False

    def map(self, _):
        return Left(self.value)

    def __str__(self):
        return 'Left (%s)' % self.value

    def __eq__(self, other):
        return Left()

    def __ne__(self, other):
        return Left()
