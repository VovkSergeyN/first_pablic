# class LinkedList:
#     def __init__(self):
#         self.head = None # ссылка на первый объект связного списка (если список пустой, то head = None);
#         self.tail = None # ссылка на последний объект связного списка (если список пустой, то tail = None)
#     def add_obj(self, obj): # добавление нового объекта obj класса ObjList в конец связного списка;
#         if self.head is None:
#             self.head = obj
#
#             self.tail = obj
#         else:
#             prev_obj = self.tail
#             self.tail = obj
#             self.tail.set_prev(prev_obj)
#             prev_obj.set_next(obj)
#     def remove_obj(self): # удаление последнего объекта из связного списка;
#         prev_obj = self.tail.get_prev()
#         if prev_obj is None:
#             self.head = None
#             self.tail = None
#         self.tail = prev_obj
#         self.tail.set_next(None)
#     def get_data(self): # получение списка из строк локального свойства __data всех объектов связного списка.
#         lst = []
#         current = self.head
#         while not (current is None):
#             lst.append(current.get_data())
#             current = current.get_next()
#         return lst
#
#
#
# class ObjList:
#     def __init__(self, data):
#         self.__next = None # ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
#         self.__prev = None # ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
#         self.__data = data
#     def set_next(self, obj): # изменение приватного свойства __next на значение obj;
#         self.__next = obj
#     def set_prev(self, obj): # изменение приватного свойства __prev на значение obj;
#         self.__prev = obj
#     def get_next(self): # получение значения приватного свойства __next;
#         return self.__next
#     def get_prev(self): # получение значения приватного свойства __prev;
#         return self.__prev
#     def set_data(self, data): # изменение приватного свойства __data на значение data;
#         self.__data = data
#     def get_data(self): # получение значения приватного свойства __data.
#         return self.__data
#
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
# print(res)

# class Counter:
#     def __init__(self, low, high):
#         self.low = low
#         self.high = high
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.low > self.high:
#             raise StopIteration
#         else:
#             self.low += 1
#             return self.low - 1
#
# c = Counter(3, 7)
# for i in c:
#     print(i)
# i = iter(lambda: 1, 0)
# for _ in range(20):
#     print(next(i))

def first():
    yield 1
    yield 2
def second():
    yield from first()
    yield 100
    yield 200
print(type(secondit))
gen = second()
print(type(gen))

for i in gen:
    print(i)