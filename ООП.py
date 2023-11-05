# class

# class название класса:
#       атрибуты класса
#        методы класса

# class Human:
#     pass
# h = Human
# print(h)

#методы класса

# class Human:
#     def say_hello(self):
#         print('hello')
# h = Human()
# h.say_hello()

# class GG:
#     def say(self, message):
#         print(message)
#     def say_hello(self):
#         self.say('hello')
# g =  GG()
# g.say_hello()


#констуркторы
# class Person:
#     def __init__(self):
#         print('create a project Person')
#     def say(self, message):
#         print(message)
# p = Person()
# p.say('hi')


#атрибуты

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 1
# p = Person("Bibi")
# print(p.age)
# print(p.name)
# p.age = 23
# print(p.age)
# p.info = 'he likes dog'
# print(p.info)

# создание объекта

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 1
#     def info(self):
#         print(f'name: {self.name}, age: {self.age}')

# bibi = Person("Bibi")
# bob = Person("BOB")
# bibi.age = 23
# bibi.info()
# print('--------------')
# bob.age = 44
# bob.info()

# принципы ООП
#ИНКАПСУЛЯЦИЯ

# class Person:
#      def __init__(self, name):
#          self.__name = name
#          self.__age = 1
#      def set_age(self, age):
#          if 1 < age < 100:
#              self.age = age
#          else:
#              print('uncorrectly yers old!')
#      def get_age(self):
#          return self.__age
#      def get_name(self):
#          return self.__name
#
#      def info(self):
#          print(f'name: {self.__name}, age: {self.__age}')
#
#
# bibi = Person("Bibi")
# bibi.info()

# НАСЛЕЛДСТВОВАНИЕ

# class Monkey:
#     name = 'boba'
#
# class Banana(Monkey):
#     def ban(self):
#         print('BOBA LIKES Banana')
#
# b = Banana()
# print(b.name)
# b.ban()

