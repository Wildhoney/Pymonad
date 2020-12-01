from .maybe import Maybe

class Nothing(Maybe):
    ok = False


    def map(self, _):
        return Nothing()

    def __str__(self):
        return 'Nothing'

