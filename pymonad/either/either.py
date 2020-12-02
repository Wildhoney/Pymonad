from pymonad.functor import Functor


class Either(Functor):
    def is_right(self):
        return self.ok

    def is_left(self):
        return not self.ok

    def get(self, default_value=None):
        if self.ok:
            return (self.value, None)
        return (default_value, self.value)
