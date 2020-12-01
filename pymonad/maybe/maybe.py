from ..functor.functor import Functor


class Maybe(Functor):
    def is_just(self):
        return self.ok

    def is_nothing(self):
        return not self.ok

    def get(self, default_value=None):
        if self.ok:
            return self.value
        return default_value
