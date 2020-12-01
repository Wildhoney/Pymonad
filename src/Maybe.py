from Base import Base


class Maybe(Base):
    def __init__(self, value):
        self.value = value

    def is_none(self):
        return self.value is None

    def is_just(self):
        return not self.is_none()

    def map(self, f):
        if self.is_none():
            return __class__(None)
        return __class__(f(self.value))

    def get(self, default_value=None):
        if self.is_none():
            return default_value
        return self.value

    def __str__(self):
        if self.is_none():
            return "Nothing"
        return 'Just (%s)' % self.value
