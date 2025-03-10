# This week, we'll consider how sets (and dictionaries, for that matter) check to see if data is hashable -- that is, can have the "hash" function run on it -- and then if it is unique.
#
# Normally, instances of user-defined classes are both hashable and unique.  For example:
#     class Foo(object):
#         def __init__(self, x):
#             self.x = x
#
#     f1 = Foo(10)
#     f2 = Foo(10)
#     f3 = Foo(10)
#
#     s = {f1, f2, f3}
#
# If we then ask for the value of s, we get:
#    {<__main__.Foo at 0x10c3da390>,
#      <__main__.Foo at 0x10c481c50>,
#      <__main__.Foo at 0x10c481c88>}
#
# In other words, these three objects are hashable, but they are also seen as distinct, even though their "x" attribute is identical.
#
# This week's exercise is a two parter:
#
# (1) Modify the "Foo" class above, such that inserting instances of Foo with identical values of "x" will be seen as the same object, and thus not added multiple times to the set.
#
# (2) Define a "Uniquish" class from which other classes can inherit, and which offers the same functionality to any subclass.  For example:
#     class Bar(Uniquish):
#         def __init__(self, x, y):
#             self.x = x
#             self.y = y
#
#     b1 = Bar(10, 'abc')
#     b2 = Bar(10, 'abc')
#     b3 = Bar(10, 'abc')
#
#     s = {b1, b2, b3}
#
# And when we look at the set, we'll see that they are seen as unique -- and thus only one instance appears.
#    >>> s
#
#     {<__main__.Bar at 0x10c4b0400>}
#
# We'll assume that all attributes in the son-of-Uniquish class are hashable, although if you wish to ignore them or otherwise deal with them, you're welcome to do so.

class Foo(object):
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        if isinstance(other, Foo):
            return self.x == other.x

        return False


f1 = Foo(10)
f2 = Foo(10)
f3 = Foo(10)

s = {f1, f2, f3}

for i in s:
    print(i)


class Uniquish:
    def __init__(self, args, *kwargs):
        self._args = args
        self._kwargs = kwargs

    def __eq__(self, other):
        if not isinstance(other, Uniquish):
            return NotImplemented
        return (self._args, self._kwargs) == (other._args, other._kwargs)

    def __hash__(self):
        return hash((self._args, tuple(sorted(self._kwargs.items()))))


class Bar(Uniquish):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y)

    def __eq__(self, other):
        if not isinstance(other, Bar):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


b1 = Bar(10, 'abc')
b2 = Bar(10, 'abc')
b3 = Bar(10, 'abe')

s = {b1, b2, b3}
print(s)
