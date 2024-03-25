"==============exception==========="
# исключения-обьекты которые прерывают работу кода,если не были обработаны



SyntaxError
#исключение которое выходит коглв в коде допущена синтексическая ошибка



"""
a=
SyntaxError
"""


NameError
#ичключение которое выходит когда вызодит когда мы обращаемся к несушествующей переменной

'''
num1=15
print(num5)
NameError
'''

IndexError
#выходит когда мы обращаемся к несушествуюшему индексу 
'''
list_=[12,20,0,2]
print(list_[1000]) pop out of range
indexerror
'''
'''
[12,0,24,'hi'].pop(1000)
indexerror pop from empty list
'''
KeyError
#исключение которое выходит когда мы обращаемся по несуществуюшему ключу


'''
dict_={'a':1}
dict_{'c'}
KeyError
'''

'''
dict_={'a':1}
dict_.get('c')
ошибки не будет если так как get не вызывает ошибку а вернет None,если нет такого ключа
'''


ValueError
#выходит когда мы передаем в функцию не корректный для нее тип данных
#когда мы расспаковываем итреррируемяй обьект на несколько переменных и кол-во переменных не совпадает с кол-во элентов

'''
a,b,c=1,2
ValueError
'''

TypeError
 #исключение выходит,когда мы пытаемся использовать методы которые не свойтвенные какому-то типу данных
# когда мы пытаемся передать функции больще или меньше аргументов чем принимает функция


'''
for i in 1234:
TypeError
'''
'''
'5'+5
TypeError
'''
'''
{[1,2,3]:'hi'}
TypeError
'''

''' input('input your data')

TypeError
'''
'''
[].append()
TypeError
'''

ZeroDivisionError
''' 
45/0
45//0
45%0
ZeroDivisionError
'''

AttributeError
#Выходит когда мы обрашаемся к не сущ аттрибуту или методу  обьекта (типа данных)

'''
'makers'.pop()
AttributeError
'''


IndentationError
#ВЫХОДИТ КОГДА МЫ НЕ ПРАВИЛЬНО ИСПОЛЬЗУЕМ ОТСТУППЫ
'''
for i in range(11):

'''

Exception 
# это исключение создали чтобы его вызывать



'============вызов исключений==============='


#raise NameError('просто вызываю NameError')
#raise KeyError('HPIH')



'==============ОБРАБОТКА ИСКЛЮЧЕНИЙ============'
#  ОБРАТБОТКА ИСКЛЮЧЕНИЙ нужна чтобы код не прекращао работу,мы можем использовать  try-except,и обрабатывать вызваннок исключение


# try:# код который может вызвать ошибку
#     num=int(input('input number'))
# except ValueError:#ожидаемая исключение
#     #обработку на исключения которое поймали
#     print('you put not number')
# else:
#     # код который отработает если иклбчения не вышло
#     print(f'you put {num} number')

# finally:
#     print('GOODBYE BITCH')

try:
    num=int(input())
    res=10/0
# except (ValueError,ZeroDivisionError):
#     print('')
except Exception as e:
    print(e)



#except : обрабатывает все исключения которые могут выйти
#except Exception


#можем указать в  except несколько исключений при помощи скобок и звпятой except(ValueError,)
    
try:
    raise NameError
except NameError:
    print(1)
    
dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
print(dict_['a'].items())