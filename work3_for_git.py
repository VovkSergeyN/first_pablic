# 18.02.2025
# class Server: # для описания работы серверов в сети;
#     IP_start = 1
#     def __init__(self):
#         self.buffer = []
#         self.ip = self.create_ip()
#         self.router = None
#
#     @classmethod
#     def create_ip(cls):
#         new_IP = cls.IP_start
#         cls.IP_start += 1
#         return new_IP
#
#     def send_data(self, data): # для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
#         if not (self.router is None):
#             self.router.buffer.append(data)
#         else:
#             print("Not connection with router")
#
#     def get_data(self): # возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;
#         push = self.buffer[:]
#         self.buffer.clear()
#         return push
#
#     def get_ip(self): # возвращает свой IP-адрес
#         return self.ip
#
# class Router: # для описания работы роутеров в сети (в данной задаче полагается один роутер);
#     def __init__(self):
#         self.buffer = [] # список для хранения принятых от серверов пакетов (объектов класса Data)
#         self.servers = {} # словарь серверов соединенных с роутером
#
#     def link(self, server): # для присоединения сервера server (объекта класса Server) к роутеру (для простоты, каждый сервер соединен только с одним роутером);
#         self.servers[server.ip] = server
#         if server.router is None:
#             server.router = self
#
#     def unlink(self, server): # для отсоединения сервера server (объекта класса Server) от роутера;
#         if server.ip in self.servers:
#             del self.link_list[server.ip]
#             server.router = None
#
#     def send_data(self): # для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам (после отправки буфер должен очищаться).
#         for data_ in self.buffer:
#             for ip, server in self.servers.items():
#                 if data_.ip == ip:
#                     server.buffer.append(data_.data)
#                     break
#
#
# class Data: # для описания пакета информации.
#     def __init__(self, data: str, ip: int):
#         self.data = data
#         self.ip = ip
#
#     # def __str__(self):
#     #     return str((self.data, self.ip))
#     def __repr__(self):
#         return str((self.data, self.ip))
#
# router = Router()
# sv_1 = Server()
# sv_2 = Server()
# router.link(sv_1)
# router.link(sv_2)
# router.link(Server())
# router.link(Server())
# print(router.servers)
# sv_5 = Server()
# router.link(sv_5)
# print(router.buffer)
#
# sv_1.send_data(Data("Hello", sv_5.get_ip()))
# sv_2.send_data(Data("Hello", sv_5.get_ip()))
# sv_5.send_data(Data("Hi", sv_1.get_ip()))
# print(router.buffer)
# router.send_data()
# msg_lst_1 = sv_1.get_data()
# msg_lst_5 = sv_5.get_data()
# print(msg_lst_1, msg_lst_5, sep='\n')


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Shape:
   def area(self):
      pass
class Rectangle(Shape):
   def __init__(self, length, breadth):
      self.length = length
      self.breadth = breadth
   def area(self):
      return self.length * self.breadth
class Circle(Shape):
   def __init__(self, radius):
      self.radius = radius
   def area(self):
      return 3.14 * self.radius * self.radius
   def area(self, diameter):
      self.radius = diameter / 2
      return 3.14 * self.radius * self.radius
r = Rectangle(5, 10)
print("Area of rectangle:", r.area())
c = Circle(7)
print("Area of circle with radius 7:", c.area())
print("Area of circle with diameter 10:", c.area(10))


x = X()
x.sub_method(1)
print('Обратите внимание как происходит инициализация')
print('классов при указании аргументов в функции super()')
y = Y()
y.sub_method(5)