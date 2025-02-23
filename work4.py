print("Hello world!!!")
date = '18.02.2025'


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
class Point2D:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y
pt2 = Point2D(10, 20)
print(pt2.x)
print(pt2.y)
print(dir(pt2))
print(pt2.__slots__)
print(type(pt2))
print(Point2D.__mro__)
"\n1erwlekrjwlkrj" 
"\n1erwlekrjwlkrj" 
"1erwlekrjwlkrj" 
