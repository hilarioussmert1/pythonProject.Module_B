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
import board as board

# print('b /= b')

# person_age = int(input('введите свой возраст:'))
# print((person_age> 18) and (person_age <= 35))


# password = "dgh36gh7"
# answer = input()

# f password == answer:
#  print("Пароль верен! Добро пожаловать.")
# else:
# print("Вы ввели неверный пароль")

nike_air_max = 100
nike_airforce = 120
puma = 70
new_balance = 110

# text = input("скажите ваш бюджет:")
# print('идет подбор кросовок...')

# if cost <= int(text):
# print("")


dictionary = {'nike_air_max ': '250$',
              'nike_airforce': '160$',
              'puma': '140$',
              'new_balance550': '179$'}


# name = input('напишите ваш бюджет:')
# print('подбираем подходящие пары..')
# if name == 200:
# print()


# month = int(input('введите месяц(цифрами):'))
# if month in [3,4,5]:
# print("It is spring")
# elif month in [6,7,8] :
# print("it is summer")
# elif month in [9,10,11]:
# print("осень")
# elif month in [1,2,12]:
# print("winter")


# def devider(n,a):
# if a % n:
#     return False
# else:
#    return True

# def quality(a):
# count = 0
# for d in range(a, a + 1):
#  if a % d == 0:
#       count += 1
# return count
# quality(5)


# text = "првивет,мир!!!!!!"
# for f in range(1,11):
# print(text)


def man(num):
    result = 1
    count = 1
    while count <= num:
        result *= count
        count += 1
        return result


# print(man(5))


def fun():
    f = 2
    while True:
        if is_fun():
            yield n
            n += 1
        # print(next)


def t_func(i_func):
    i_func()
    i_func()


def hello():
    print('Hello')


# a = [1,2,'hello','hi',[4,5,'bro']]
# for i in a:
#    if type(i) == list:
#        for l in i:
#            print(l)
# else:
#        print(i)


# a = 'b'
# if b==0:
# else:
# print('нет')
# while b == 0:
#  break


# lst = [-15,2,100,4,5,6,-12]
# new_list = []
# for i in lst:
#  if abs(i)>5:
#     new_list.append(i)
# print(new_list)


# lst = [-15,2,100,424,5,6,-12]
# max = lst[0]
# for i in range(1,len(lst)):
# if lst[i] > max:
#      max = lst[i]
# print(max)


# n = 5
# h =str()
# for i in range(1,11):
#     a = n*i
#     h = h + f'{n}*{i} = {a}\n'
# print(h)


# def say_hello(name,age,city):
#     print(f'hello,{name},age :{age},city:{city}')
# say_hello('bob','17 years old','Melbourne')

# def sum(*num):
#     count = 0
#     for i in num:
#         count += i
#     print(f'sum:{count}')
# sum(1,2,3,4,5,65,7)
# sum(6,9,34,5)


# def double(num):
#     return 2 * num
# print(double( 379))


# def message(a,b): print(a+b)
# say = message
# say(1,2)
#
# def messege(a,b):
#     print(a*b)
# messege(2,2)

# def do_operation(a,b, operation):
#     result = operation(a,b)
#     print(f'result:{result}')
# def sum(a,b): return a+b
# def mult(a,b): return a*b
#
# do_operation(3,3,sum)
# do_operation(3,3,mult)

# def sum(a,b): return a+b
# def mult(a,b): return a*b
#
#
# def select(choice):
#         if choice == 1:
#             return sum
#         elif choice == 2:
#             return mult
#
# operation = select(1)
# print(operation(9,6))

# recursia

# def rec(s):
#     if s <4:
#         print(s)
#         rec(s+1)
#         print(s)
# rec(1)


# generator spiska


# a = [i ** 2 for i in range(1,6)]
#
# #выражение генератора
# b = ( i ** 2 for i in range(1,6))
# print(b)

# s = [1,2,3]
# d = iter(s)
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))

# b = ( i ** 2 for i in range(1,6))
# print(sum(b))


# c = ( i for i in range(1000000))
# for i in c:
#     print(i)

# yield

# def cube_num(nums):
#     cube_list =[]
#     for i in nums:
#         cube_list.append(i**3)
#     return cube_list
# cub = (cube_num([1,2,3,4,5,6,7,8,9]))
# print(cub)


# def cube_num(nums):
#    for i in nums:
#        yield(i**3)
# cub = (cube_num([1,2,3,4,5,6,7,8,9]))
# print(*cub)
#
# def my_decorate(func):
#     def wrapper(n):
#         print('start')
#         func(n)
#         print('end')
#     return wrapper
# @my_decorate
# def my_func(numbers):
#         print(numbers ** 2 )
# my_func(7)
#

# a = input('введите число')
# if a is not float:
#     print('a целое число')
#     if int(a) > 99 and int(a) < 1000:
#         print('a входит в диапозон')
#         if int(a) % 2 == 0 and int(a) % 3 == 0:
#             print('a кратно 2 и 3')
#         else:
#             print('a не кратно 2 и 3')
#
# else:
#         print('a не целое число')
# print('end')

# a = input('введите число')
# if type(a) == int and 99 < int(a) < 1000 and a % 2 == 0 and a % 3 == 0:
#     print("Число удовлетворяет условиям")

# a = int(input('введите число'))
# if all([type(a) == int,
#         100 <= int(a) <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print("Число удовлетворяет условиям")
#
# b = int(input())
# if all([type(b) == int,
#         100 < b,
#         b % 2 == 0]):
#     print("Число удовлетворяет условиям")
#

#

# L = list(map(int, input().split()))
#
# print(not any(L))


# gg = input("boba")
#
# a = [int(i) for i in gg.split()]
# print(a)

# L = [i for i in range(10)]
# M = [i for i in range(10,0,-1)]
# c = [a*b for a,b in zip(L,M)]
# print(c)

# text = input()
#
# last = text[0]
# count = 0
# result = ''
# for c in text:
#      if c == last:
#         count += 1
#      else:
#         result += last + str(count)
#         last = c
#         count = 1
#
# result += last + str(count)
# print(result)

# text = input()
# last = text[0]
# count = 0
# result = ''
# for c in text:
#     if c == last:
#         count += 1
#     else:
#         result += last + str(count)
#         last = c
#         count = 1
#
# result += last + str(count)
# print(result)
#


# import time
#
# def decorate(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         print(time.time() - start_time)
#     return wrapper
#
# @decorate
# def sp():
#     spisok = [i ** 2 for i in range(10000) if i % 2 == 0]
#    #print(spisok)
#
# sp()

# text = input('text:')
#     for i in text:
#     print()

# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower,L)))
#
#
# def good(x):
#     return x % 2 == 0
#
# result = filter(good, [-2, -1, 0, 1, -3, 2, -3])
#
# print(list(result))


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
#


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# Peter = User(name = 'Peter Robertson',email = 'peterrobertson123@gamil.com')
# julia = User(name = 'Julia Donaldson',email = 'juliadonald@gmail.com')
#
# print(peter.name)
# print(julia.email)

class person():
    def __init__(self, name):
        self.name = name
        self.age = 12


tom = person('Tom')
print(tom.age)
print(tom.name)



# def f():
#     return [1, 2, 3], ["a", "b", "c"]
# list1, list2 = f()

game_field = [[0]*6]*6


# def draw_board(game_field):
#     for i in range(1, 7):
#         for j in range(1, 7):
#             print(j, end=" ")
#         print()
#
#
# draw_board(game_field)


# game_field = [[0]*6]*6
#
# def draw_board(game_field):
#     for j in range(0, 6):
#         for i in range(0, 6):
#          print(str(game_field[j][i]) + '|')
#         print("\n")
#
# draw_board(game_field)
