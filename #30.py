def betterrepr(cls):

    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = vars(self)
        return f"Instance of {class_name}, vars = {attributes}"

    cls.__repr__ = __repr__
    return cls

@betterrepr
class Foo:
    def __init__(self,x,y):
        self.x = x
        self.y = y


f = Foo(10,[1,2,3,4])
print(f)