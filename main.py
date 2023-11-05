# board = list(range(1, 10))
#
# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
#         print("-" * 13)
#
#
# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token + "? ")
#         try:
#             player_answer = int(player_answer)
#         except ValueError:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if 1 <= player_answer <= 9:
#             if str(board[player_answer - 1]) not in "XO":
#                 board[player_answer - 1] = player_token
#                 valid = True
#             else:
#                 print("Эта клетка уже занята!")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9.")
#
#
# def check_win(board):
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False
#
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#
#         tmp = check_win(board)
#         if tmp:
#             print(tmp, "выиграл!")
#             win = True
#             break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
#
#
# main(board)
#
# input("Нажмите Enter для выхода!")


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# Peter = User(name = 'Peter Robertson',email = 'peterrobertson123@gamil.com')
# julia = User(name = 'Julia Donaldson',email = 'juliadonald@gmail.com')
#
# print(Peter.name)
# print(julia.email)

# конструкторы
# class person:
#     def __init__(self):
#         print('create obj person')
#     def say_hello(self, message):
#             print(message)
# tom = person()
# tom.say_hello('hello')
#

# class person():
#     def __init__(self, name):
#         self.name = name
#         self.age = 12
#     def display_info(self):
#         print(f'name:{self.name},age: {self.age}')
# tom = person('Tom')
# tom.display_info()


# class Person:
#     def __init__(self, name):
#             self.__name = name
#             self.__age = 1
#     def set_age(self, age):
#         if 1 < age < 100:
#                 self.__age = age
#         else:
#                 print('uncorectly age')
#     def get_age(self):
#             return self.__age
#     def get_name(self):
#             return self.__name
#     def display_info(self):
#         print(f'name:{self.__name},age: {self.__age}')
# tom = Person('Tom')
# tom.display_info()
# tom.set_age(-1234)
# tom.get_age()
# tom.get_name()
# tom.__age = 24
# print(tom.__age)

# ИНКАПСУЛЯЦИЯ

# class computer:
#     def __init__(self):
#         self.__maxprice = 900
#     def sell(self):
#         print(f'finish cost: {self.__maxprice}')
#     def setmax(self, price):
#         self.__maxprice = price
#
# c = computer()
# c.sell()
#
# c.__maxprice = 1000
# c.sell()
#
# c.setmax(1000)
# c.sell()
#
# ПОЛЕМОРФИЗМ
# одна функция для разных форм(типов данных)

# class parrot:
#      def fly(self):
#             print('parrot can fly')
#      def swim(self):
#             print('parrot can not swim')
# class penguin:
#      def fly(self):
#          print('penguin can not fly')
#      def swim(self):
#          print('penguin can  swim')
#
#  #общий интерфейс
# def flyingtest(bird):
#      bird.swim()
# kesha = parrot()
# pasha = penguin()
# flyingtest(kesha)
# flyingtest(pasha)


# Наследование!!!!

# class geom:
#     name = 'geom'
# class line(geom):
#     def draw(self):
#         print('рисование')
#
#         def set_coords(self, x1, y1, x2, y2):
#             self.x1 = x1
#             self.x2 = x2
#             self.y1 = y1
#             self.y2 = y2
#             self.draw()
# class rect(geom):
#         def draw(self):
#             print('рисование прямоугольника')
#
# g = geom
# l = line()
# r = rect()
# g.set_coords(0,0,0,0)
# l.set_coords(1,1,2,2)
# r.set_coords(2,3,4,5)
# print(l.__dict__)
# print(r.__dict__)

# setter and getter
# class Person:
#     def __init__(self, name):
#             self.__name = name
#             self.__age = 1
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if 1 < age < 100:
#                 self.__age = age
#         else:
#                 print('uncorectly age')
#     @property
#     def name(self):
#             return self.__name
#     def display_info(self):
#         print(f'name:{self.__name},age: {self.__age}')
# tom = Person('Tom')
# tom.display_info()
# tom.age = 12
# tom.display_info()


# class human:
#     age = None
#     def __init__(self):
#          self.age = age
#     def get_age(self, age = 2):
#          return self.age
#     def set_age(self, age):
#          if age > 0:
#              self.age = age
#
# h = human()
# h.set_age(12)
# print(h.get_age())


# class Cat:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_gender(self):
#         return self.gender
#
#     def get_age(self):
#         return self.age
#
# class Dog(Cat):
#     def get_pet(self):
#        return f'{self.get_name()}{self.get_age()}'
#
# dog1 = Dog('Felix', 'boy',' 0')
#
# print(dog1.get_pet())
#
#
# class Rectangle:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def get_area(self):
#         return self.a * self.b
#
#
# rect_1 = Rectangle(3, 4)
# rect_2 = Rectangle(12, 6)
# print(rect_1.get_area())
# print(rect_2.get_area())

# class Lion:
#     def __init__(self,name):
#         self.name = name
#     def __repr__(self):
#         return f'Lion - {self.name}'
#
#     def __str__(self):
#         return f'Lion - {self.name}'
# l = Lion('misha')
# print(l)

# class Rectangle:
#     def __init__(self,x,y, width,height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return f'Rectangle: x = { self.x}, y = {self.y}, width = {self.width}, height = {self.height}'
#     def get_area(self):
#         return self.width * self.height
#
# r = Rectangle(5,10,50,100)
# print(r)
# print(r.get_area())
#
# class Client():
#     def __init__(self, name, surname, city, balance):
#         self.name = name
#         self.surname = surname
#         self.city = city
#         self.balance = balance
#
#     def __str__(self):
#         return f'<<{self.name} {self.surname}.{self.city}.Balance:{self.balance} rub.>>'
#
#     def guest(self):
#         return f'{self.name},{self.surname},{self.city}.'
#
# c = Client('Ivan','Petrov','Moscow','50')
# c1 = Client('Pasha','Ivanov','Novosibirsk','50')
# c2 = Client('Sasha','Romanovich','Novosibirsk','50')
#
# guest_list = [c,c1,c2]
#
# for i in guest_list:
#     print(i.guest())
#
# class square:
#     def __init__(self, side):
#         self.side = side
#
# class SquareFactory:
#
#     @staticmethod
#     def create_square(side):
#         return square(side)
#
#
# c = SquareFactory.create_square(4)
# print(c.side)
#
# try:
#     a = int(input('введите:'))
#     print(a)
# except ValueError as r:
#     print('Вы ввели неправильное число')
# else:
#     print('вы ввели' + int(a))
# finally:
#     print('Выход из программы')


# def  draw_arena( arena):
#     list = '  | 1 | 2 | 3 | 4 | 5 | 6 |'
#     print(list)
#     for i in range(7):
#         print(arena[i + 1],'|',arena[0],'|',arena[0],'|',arena[0],'|',arena[0],'|',arena[0],'|',arena[0],'|')
#
#
# draw_arena(' 123456')

# game_field = [[0]*6]*6
#
# def draw_board(game_field):
#         for i in range(1, 7):
#             for j in range(1, 7):
#                 print(j, end=" ")
#             print()
#
# draw_board(game_field)


# board = list(range(1, 10))
#
# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print("|", board[0 + i * 1], "|", board[1 + i * 2], "|", board[2 + i * 3], "|")
#         print("-" * 13)
# draw_board(board)

import random


class Robot:

    def __init__(self):
        self.robots_turns = []

    def get_robot_turns(self):
        return self.robots_turns

    def add_robot_turn(self, i, j):
        robot_turns.append(i, j)


class Ship:

    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def check(self):
        if self.width == 1:
            print('вы выбрали одинарный корабль!')
        elif self.width == 2:
            print('вы выбрали двойной корабль!')
        elif self.width == 3:
            print('вы выбрали тройной корабль!')
        else:
            print('wrong answer!')

    def validate_ship_position(self, start_point_i, start_point_j, width, horisontal_or_vertical, game_field):
        if start_point_i < 1 or start_point_j < 1 or start_point_i > 6 or start_point_j > 6:
            return False
        if horisontal_or_vertical == 0 and start_point_j + width - 1 > 6:
            return False
        if horisontal_or_vertical == 1 and start_point_i + width - 1 > 6:
            return False

        if horisontal_or_vertical == 0:
            for k in range(start_point_j, start_point_j + self.width):
                if (game_field[start_point_i - 1][k - 1] == 1):
                    return False
        else:
            for k in range(start_point_i, start_point_i + self.width):
                if game_field[k - 1][start_point_j - 1] == 1:
                    return False
        return True

    def position_ship_by_user(self, game_field):
        i = -1
        j = -1
        horisontal_or_vertical = -1

        while not self.validate_ship_position(i, j, self.width, horisontal_or_vertical, game_field):
            i = int(input('первая координата куда хотите поставить начальную точку корабля?'))
            j = int(input('вторая координата куда хотите поставить начальную точку корабля?'))
            if self.width > 1:
                horisontal_or_vertical = int(input('горизонтально(0) или вертикально(1)?'))

        if horisontal_or_vertical == 0:
            for k in range(j, j + self.width):
                game_field[i - 1][k - 1] = 1
        else:
            for k in range(i, i + self.width):
                game_field[k - 1][j - 1] = 1

    def position_ship_by_robot(self, game_field):
        i = -1
        j = -1
        horisontal_or_vertical = -1

        while not self.validate_ship_position(i, j, self.width, horisontal_or_vertical, game_field):
            i = random.randint(0, 6)
            j = random.randint(0, 6)
            if self.width > 1:
                horisontal_or_vertical = random.randint(0, 1)

        if horisontal_or_vertical == 0:
            for k in range(j, j + self.width):
                game_field[i - 1][k - 1] = 1
        else:
            for k in range(i, i + self.width):
                game_field[k - 1][j - 1] = 1


class Game:

    def __init__(self):
        self.game_field = [[0 for i in range(6)] for j in range(6)]
        self.game_field_robot = [[0 for a in range(6)] for b in range(6)]

    def get_game_field(self):
        return self.game_field

    def get_game_field_robot(self):
        return self.game_field_robot

    def attack(self, i, j, game_field):
        if self.game_field[i - 1][j - 1] == 1:
            self.game_field[i - 1][j - 1] = 2
            print('Hit!')
            return True
        elif self.game_field[i-1][j-1] == 'X':
            print("You guessed that one already.")
        else:
            print('Missed!')
            game_field[i-1][j-1] = 'X'
            return False


    def start(self):

        player_succes_count = 0
        robot_succes_count = 0

        valid = False
        while not valid:

            print('ваш ход!')
            i = int(input('куда ударим по i:'))
            print(i)
            j = int(input('куда ударим по j:'))
            print(j)
            if self.attack(i, j, self.game_field):
                player_succes_count += 1

            print("Ходит робот!")
            i = random.randint(0, 6)
            j = random.randint(0, 6)
            if self.attack(i, j, self.game_field_robot):
                robot_succes_count += 1


            if player_succes_count == 11:
                print('Player  is winner!')
                valid = True
            elif robot_succes_count == 11:
                print('Robot  is winner!')
                valid = True

    def draw_board(self):
        print(" Your field")
        print(" |1|2|3|4|5|6|")
        for j in range(0, 6):
            line_str = str(j + 1) + '|'
            for i in range(0, 6):
                line_str = line_str + str(self.game_field[j][i]) + '|'
            print(line_str)

    def draw_board_robot(self):
        print()
        print(" Robot's field")
        print(" |1|2|3|4|5|6|")
        for j in range(0, 6):
            line_str = str(j + 1) + '|'
            for i in range(0, 6):
                line_str = line_str + str(self.game_field_robot[j][i]) + '|'
            print(line_str)


game = Game()
game.draw_board()
game.draw_board_robot()

s = Ship(3)
s.check()
s.position_ship_by_user(game.get_game_field())

for i in range(2):
    s = Ship(2)
    s.check()
    s.position_ship_by_user(game.get_game_field())
for i in range(4):
    s = Ship(1)
    s.check()
    s.position_ship_by_user(game.get_game_field())

s = Ship(3)
s.position_ship_by_robot(game.get_game_field_robot())

for i in range(2):
    s = Ship(2)
    s.position_ship_by_robot(game.get_game_field_robot())
for i in range(5):
    s = Ship(1)
    s.position_ship_by_robot(game.get_game_field_robot())

game.start()

draw_board(game.get_game_field())
draw_board_robot(game.get_game_field_robot())

# class Human:
#     def init_human(self,age,name):
#         self.age = age
#         self.name = name

#     def get_age(self,age):
#         return self.age
#
#     def get_name(self, name):
#         return self.name
#     def set_age(self,age,name):
#         self.name = name
#         if age > 0 and isinstance(age,int):
#             self.age = age
#     def display_info(self):
#         print('___________________________________')
#         print(f'name:{self.name}, age:{self.age}')
#         print('___________________________________')
#
# h = Human()
# h.set_age(17,'Tim')
# h.display_info()


# a = int(input('Куда хотите стрельнуть первую точку(по j)'))
# b = int(input('Куда хотите стрельнуть первую точку(по i)'))
#
# if game_field_1 == 1:
#     print('Hit')
# elif game_field_1 == 0:
#     print('Miss')

# while True:
#     for turn in range(7):
#         print()
#     guess_i = int(input('guess i row:'))
#     guess_j = int(input('guess j row:'))
#     if guess_i == ship_i and guess_j == ship_j:
#         print('hit')
#         return True
#     else:
#         if (guess_i < 0 or guess_i >= 7) or (guess_j < 0 or guess_j >= 7):
#             print("Oops, that's not even in the ocean.")
#         elif (game_field_1[guess_i][guess_j] == "X"):
#             print("You guessed that one already.")
#         else:
#             print("You missed !")
#             game_field_1[ship_i][ship_j] = "X"
#             continue
#         if (turn == 3):
#             if 1 not in draw_board_robot:
#                 print('Ход бота!')
#                 guess_i = random.randint(0, 5)
#                 guess_j = random.randint(0, 5)
#                 if guess_i == ship_i and guess_j == ship_j:
#                     print('Your Turn!')
#                     game_field[ship_i][ship_j] = "X"
#                     print('Your Turn!')
#                 elif game_field_1[ship_i][ship_j]:
#                     print('bot had miss!')

# class Foo:
#     def __init__(self):
#         pass
#
#     def method1(self):
#         print('Method 1')
#
#     def method2(self):
#         print('Method 2')
#         self.method1()
# #
# f = Foo()

# f.method1()
# f.method2()
#   def attack(self, i, j, gm):
#         if gm[i][j] == 1:
#             gm[i][j] = 2
#             print('Hit!')
#             return True
#         elif(game_field_1[i][j] == "X"):
#              print("You guessed that one already.")
#         else:
#             print('Miss!')
#             game_field_1[i][j] ='X'
#             return False
#
#     def start(self):
#
#         Robot(game_field_1)
#         Ship(game_field)
#
#         while True:
#             print('Your Tern')
#             i = int(input('guess i:'))
#             j = int(input('guess j:'))
#             if not self.attack(i, j, game_field_1):
#                 break
#             if self.check_win(game_field_1):
#                 print('player first is winner!')
#                 break
#
#             print("robot's turn!")
#             i = random.randint(0, 6)
#             print(i)
#             j = random.randint(0, 6)
#             print(j)
#             if not self.attack(i, j, game_field):
#                 break
#             if self.check_win(game_field):
#                 print('Player second is winner!')
#                 break
#
#     def check_win(self, gm):
#         for row in gm:
#             for cell in row:
#                 if cell == 1:
#                     return False
#                 return True

# def __int__(self, i, j):
#          self.i = i
#          self.j = j
#
#      def __eq__(self, other):
#          if not isinstance(other, Dot):
#              raise TypeError(f'{other}It is a dot! ')
#          return self.i == other.i and self.j == other.j
#
#      def return_dot(self):
#          list_dot = []
#          i = self.point.i
#          j = self.point.j
#          i = 0
#          while i < self.width:
#              if self.direction == 'Г':
#                point_ship = i, j
#                list_dot.append(point_ship)
#                i += 1
#                j += 1
#          else:
#              point_ship = i, j
#              list_dot.append(point_ship)
#              i += 1
#              j += 1
#          return list_dot
