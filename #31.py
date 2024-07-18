def betterrepr(newstr=None, newrepr=None):
    def decorator_class(cls):
        if newrepr is None:
            def default_repr(self):
                class_name = self.__class__.__name__
                attributes = vars(self)
                return f"Instance of {class_name}, vars = {attributes}"

            cls.__repr__ = default_repr
        else:
            cls.__repr__ = newrepr

        if newstr is not None:
            cls.__str__ = newstr

        return cls

    return decorator_class


@betterrepr()
class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


f = Foo(10, [1, 2, 3, 4, 5])
print(f)
print(repr(f))


@betterrepr(newstr=lambda self: f"Foo with x = {self.x} and y = {self.y}")
class Bar:
    def __init__(self, x, y):
        self.x = x
        self.y = y


b = Bar(20, [6, 7, 8, 9, 10])
print(b)
print(repr(b))
