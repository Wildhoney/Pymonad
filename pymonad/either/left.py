from .either import Either


class Left(Either):
    ok = False

    def map(self, _):
        return Left(self.value)

    def __str__(self):
        return 'Left (%s)' % self.value
