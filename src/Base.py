class Base:
    def __rshift__(self, value):
        return self.map(value)

    def __or__(self, default_value):
        return self.get(default_value)
