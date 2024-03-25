#dict-изменяемый,итерируемый,неупрорядоченный,неиндексируемый тип данных для хранения данныз в параx


# user={"name":"Anonym","age":30,'last_name':'Makers'}
# print(user['name'])#Anonym
# print(user['age'])#30
# print(user["last_name"])#Makers


#ключами в словаре могут быть только неизменякмык типы данных
#ключи в словарях должны быть уникальными


'==============создание словарей========================='

# dict_={'a':1,'b':2}

# dict_=dict([('a',1),("b",2)])
# print(dict_)
dict_=dict(['a1','b2','c3'])
 #print(dict_)#{'a':1,'b':2,'c':3}
dict_={}


dict_['name']='makers'
dict_['age']=50
dict_['last_name']='bootcamp'
print(dict_)


'=====================методы словарей===================='


'get -это метод получает значение по ключу,если значение ключа нет,то выходит None по умалчанию,мы можем его поменять'

user={"name":"Anonym",
      'age':15,
      "last_ name":"Makers"}
#print(dict_['id'])#error
print(user.get("id",'такого ключа нет'))
'такого ключа нет'


"pop-удаляет пару по ключу и возвращает значение"

# dict_={'a':1,'b':2,'c':3}
# popped=dict_.pop("b")
# print(popped)
# print(dict_)

"popitem- удаляет пару и возвращает ее"

# dict_={'a':1,"b":2,"c":3}
# popped=dict_.popitem()
# print(dict_)#{}
# print(popped)#("c":3)


"update-расширяет словарь парами из второго словаря"

# dict_1={1:"a",2:"a"}
# dict_2={2:"b",3:"b"}
# dict_1.update(dict_2)
# print(dict_1)#{1:a,2:b,3:"b"}


# 'clear-очищает словарь'

# dict_={"a":1,"b":2,'c':3}
# dict_.clear()
# print(dict_)



"fromkeys-это метод для создания нового словаря используя список ключей"
#dict_=dict.fromkeys('hi')
#print(dict_)

#dict_2=dict.fromkeys(['hi',123,True],0)
#print(dict_2)

'keys,values,items'

'keys-возращает все ключи'
'values-возвращет все значения'
"items-метод который возвращает пары ключь и значение в виде  tuple"



# user={
#   'name':"Anonym",
#   "age":15,
#   "last_name":'Makers'
#  }
# list_=user.keys()
# print(user.keys())#(['name', 'age', 'last_name'])
# print(user.values())#(['name', 'age', 'last_name'])
# print(user.items())#(['name', 'age', 'last_name'])

"============итерирование словарей==============="


# user={
#   'name':"Anonym",
#   "age":15,
#   "last_name":'Makers'
#  }


# for key in user: #при итерации словаря приходит ключи
#     print(key)

#при итерации словаря методом value() приходят значение
# for values in user.values():
#     print(values)


# for k,v in user.items():
#     print(f"key {k},values{v}")







# for item in user.its():
#     print(item)
#при итерации словаря с методом items() приходит tuple c ключом и значением


user_dict={1:'a',2:"b"}
dict_2={}
for m,n in user_dict.items():
    dict_2[n]=m

print(dict_2)







print(dir(tuple))



