class PercentageTooLowError(ValueError):
    pass


class PercentageTooHighError(ValueError):
    pass


class Percentage():
    def __init__(self):
        self._values = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            value = int(value)
        if value < 0:
            raise PercentageTooLowError("Percentage can not be lower than 100")
        elif value > 100:
            raise PercentageTooHighError("Percentage can not be higher than 100")
        self._values[instance] = value


class Foo:
    participation = Percentage()


f1 = Foo()
f1.participation = 30
f2 = Foo()
f2.participation = 50
print(f1.participation)
