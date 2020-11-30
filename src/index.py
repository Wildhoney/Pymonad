class Maybe:
    def __init__(self, value):
        self.value = value

    def is_none(self):
        return self.value is None

    def is_just(self):
        return not self.is_none()

    def map(self, f):
        if self.is_none(): return Maybe(None)
        return Maybe(f(self.value))

    def get(self, default_value = None):
        if self.is_none(): return default_value
        return self.value

    def __rshift__(self, value):
        return self.map(value)

    def __or__(self, default_value):
        return self.get(default_value)

    def __str__(self):
        if self.is_none(): return "Nothing"
        return 'Just (%s)' % self.value
