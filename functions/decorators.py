"========================Декараторы===================="
#ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА-ФУНКЦИЯБ,КОТОРАЯ ПРИНИМАЕТ В АРГУМЕНТЫ ФУНКЦИЮ ДРУГУЮ,СОЗДАЕТ ВНУТРИ СЕБЯ ФУНКЦИЮ,ВЫЗЫВАЕТ ВНУТРИ ДРУГУЮ ФУНКЦИЮ


# def func1():
#     pass


# def func2( a):# aфункцию вышего порядка так как принимает друггую функцию в аргументы
#     a()


# #декараторы-функция высшего порядка,которая нужна расширить функционал функции не изменяя ее (функция обертка)
# def glushitel(func):
#     def wrapper(*args,**kwargs):
#         text=func(*args,**kwargs)
#         return text+'тихо'
    

#     return wrapper
# def gun():
#     return 'стреляет'

# wrapper=glushitel(gun)
# result=wrapper()
# print(result)

# def glushitel(func):
#     def wrapper(*args, **kwargs):
#         text = func()
#         return text + ' тихо'
#     return wrapper
# @glushitel
# def gun():
#     return 'стреляет'
# result = gun()
# print(result)


# from datetime import datetime
# def func_start_time(func):
#     def wrapper():
#         time=datetime.now().strftime('%d.%m.%Y %H:%M')
#         print(f'наша функция запустилась {time}')
#         func()
#     return wrapper


# @func_start_time
# def func():
#     print('hi')


# @func_start_time
# def func1():
#     print('hello')

# func()
# func1()



def hello():
    print



















