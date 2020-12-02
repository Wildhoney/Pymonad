from . import Maybe


class Nothing(Maybe):
    ok = False

    def map(self, _):
        return Nothing()

    def __str__(self):
        return 'Nothing'

    def __eq__(self, other):
        return Nothing()

    def __ne__(self, other):
        return Nothing()
