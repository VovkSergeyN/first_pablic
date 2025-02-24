# print("Hello world!!!")
# date = '18.02.2025'


# # x = 0
# def outer():
#     # global x
#     x = 1
#     def inner():
#         nonlocal x
#         x
#     inner()
#     print(x)
#
# print(outer())
# from collections import namedtuple
#
# Car = namedtuple("Car_from_Germany", 'mark, age, firm')
# bmw = Car("B2000", 2006, 'bmw')
# bmw2 = bmw._replace(age=2007)
# print(bmw._asdict())
# print(bmw.mark, bmw.age, bmw.firm, sep="\n")
# print(bmw2._asdict())
#
# class NegativeAgeError(Exception):
#     pass
# try:
#     raise NegativeAgeError("Age can't be negative!!!")
# except NegativeAgeError as e:
#     print(e)
#     print(dir(e))
#     print(type(e))
#     print(e.__traceback__)
#     print(e.args)

# class A():
# class A:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# a = A(1, 19)
# print(a)
# print(a.__dict__)

# ___________________________________________________________-
# class Point2D:
#     __slots__ = ("x", "y")
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# pt2 = Point2D(10, 20)
# print(pt2.x)
# print(pt2.y)
# print(dir(pt2))
# print(pt2.__slots__)
# print(type(pt2))
# print(Point2D.__mro__)
# ______________________________________________________________-
# class attr_cls:
#     def __init__(self, value, get_change="INIT"):
#         self.value = value
#         self.get_change = get_change

    # def getattr(self, name):
    #     return getattr(self.value, name)
    #
    # def repr(self):
    #     return str(self.value)
    #
    # def bool(self):
    #     return bool(self.value)
    #
    # def call(self):
    #     return self.value()
    #
    # def eq(self, other):
    #     return self.value == other
    #
    # def add(self, other):
    #     return self.value + other
    #
    # def sub(self, other):
    #     return self.value - other
    #
    # def mul(self, other):
    #     return self.value * other
    #
    # def truediv(self, other):
    #     return self.value / other
    #
    # def radd(self, other):
    #     return other + self.value
    #
    # def rsub(self, other):
    #     return other - self.value
    #
    # def rmul(self, other):
    #     return other * self.value
    #
    # def rtruediv(self, other):
    #     return other / self.value

# a = attr_cls(10)
# print(a.__dict__)
#_____________________________________________________
def change_detection(cls):
    class attr_cls():
        def init(self, value, get_change='INIT'):
            self.value = value
            self.get_change = get_change

        def getattr(self, name):
            return getattr(self.value, name)

        def repr(self):
            return str(self.value)

        def bool(self):
            return bool(self.value)

        def call(self):
            return self.value()

        def eq(self, other):
            return self.value == other

        def add(self, other):
            return self.value + other

        def sub(self, other):
            return self.value - other

        def mul(self, other):
            return self.value * other

        def truediv(self, other):
            return self.value / other

        def radd(self, other):
            return other + self.value

        def rsub(self, other):
            return other - self.value

        def rmul(self, other):
            return other * self.value

        def rtruediv(self, other):
            return other / self.value

    def getattribute(self, name):
        try:
            attr = super(cls, self).getattribute(name)
            if type(attr) != attr_cls:
                new_attr = attr_cls(attr)
                super(cls, self).setattr(name, new_attr)
                return new_attr
            return attr
        except:
            return attr_cls(None, '')

    def setattr(self, name, value):
        target = getattr(self, name, None)
        if type(target) != attr_cls or not target.get_change:
            super(cls, self).setattr(name, attr_cls(value))
        elif target.value != value or type(target.value) != type(value):
            target.value = value
            target.get_change = 'MOD'

    def delattr(self, name):
        target = getattr(self, name)
        target.value = None
        target.get_change = 'DEL'

    setattr(cls, 'setattr', setattr)
    setattr(cls, 'getattribute', getattribute)
    setattr(cls, 'delattr', delattr)

    return cls
