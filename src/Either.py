import sys
import types
from Base import Base


class Either(Base):
    def __init__(self, value, error=None):
        self.value = value
        self.error = error

    def is_right(self):
        return not self.error

    def is_left(self):
        return not self.is_right()

    def map(self, f):
        if self.is_left():
            return Either(None, self.error)
        try:
            return Either(f(self.value))
        except:
            error = sys.exc_info()[0]
            return Either(None, error)

    def get(self, default_value=None):
        is_function = (isinstance(default_value, types.FunctionType))

        if self.is_left():
            if not is_function:
                return default_value
            return default_value(self.error)
        return self.value

    def __str__(self):
        if self.is_left():
            return "Left (%s)" % self.error
        return 'Right (%s)' % self.value
