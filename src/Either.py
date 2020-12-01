import sys
import types
from Base import Base


class Either(Base):
    def __init__(self, value):
        self.value = value

    def is_right(self):
        return not isinstance(self.value, Exception)

    def is_left(self):
        return not self.is_right()

    def map(self, f):
        print(self.is_left(), self.value)

        if self.is_left():
            return __class__(self.value)

        # try:
            return __class__(f(self.value))
        # except:
        #     error = sys.exc_info()[0]
        #     return __class__(error)

    def get(self, default_value=None):
        is_function = (isinstance(default_value, types.FunctionType))

        if self.is_left():
            if not is_function:
                return default_value
            return default_value(self.value)
        return self.value

    def __str__(self):
        if self.is_left():
            return "Left (%s)" % self.value
        return 'Right (%s)' % self.value
