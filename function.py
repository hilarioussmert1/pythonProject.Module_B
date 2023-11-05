#  Локальные функции
def say():
    def say_hi(): print('hi')
    def say_bye(): print('bye')
    say_hi()
    say_bye()
# say()


#параметры функции
def say_hello(name,age):
    print(f'hello, {name}!, age: {age}')
# say_hello('Ivan', 23)

def say_hello():
    name = input('what are your name?')
    age = input('how old are you?')
    print(f'hello, {name}, age: {age}!')
# say_hello()



# неопределенное кол-во параметров

def sum(*num):
    count = 0
    for i in num:
        count += i
        double = count * 2
    print(f'sum: {double}')
sum(1,2,4,5,6,7)

#return

def get_message():
    return 'Hello'
# print(get_message()

# функции как тип
def say_hello(): print('hello')
gg = say_hello
# gg()


def sum(a, b): return a + b
def mult(a, b): return a * b
oper = sum(2, 5)
print(oper)

oper = mult
print(oper(3, 5))

#функция как параметр функуции

def do_oper(a, b , oper):
    result = oper(a, b)
    print(f'result: {result}')
def sum(a, b): return a + b
def mult(a, b): return a * b

do_oper(3,4, sum)
do_oper(2, 6, mult)

#функция как результат функции

def sum(a, b): return a + b
def mult(a, b): return a * b

def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return mult

#operation = select_operation(2)
#print(operation(5, 12))
# Рекурсия!
def rec(x):
    if x < 6:
        print(x)
        rec(x + 1)
        print(x)
# rec(2)

# Итераторы и генераторы!
# генератор списка
a = [i ** 2 for i in range(1, 7)]
print(a)
#выражения генератора
# b = (i ** 2 for i in range(1, 7))
# for i in b:
#     print(i)
#     for i in b:
#         print(i)


# #  iter!
# s = [1, 2, 3, 4, 5]

# d = iter(s)
#print(next(d))
#
# b = (i for i in range(100000))
# for i in b:
# #print(i)

# yeild!

# def double_nums(nums):
#     list_2 = []
#     for i in nums:
#         list_2.append(i ** 2)
#     return list_2
# print(double_nums([2, 4, 6, 8]))


def double_nums(nums):
    for i in nums:
        yield (i ** 2)
c = double_nums([2, 4, 6, 8])
print(*c)
