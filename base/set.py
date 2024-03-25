
'===============================================Set================================='
#множества - изменяемый, неупорядочный,итерируемый тип данных предназначенный для хранения
 #уникальных значений, множества могут хранить в себе только неизменяемый тип данных.фЕсли внутри set используется tuple то и внутри тюпл должны быть неизменяемый типы данных  ({'1,2,3,4, ('str), 12, Truee})
#в Set работает в правило - f10 (first in first out)


set_1={1,2,True,"hi"}#TRUE
set_2={True,1,"hi",2}#1



"===================FIFO/LIFO=========================="


#FIFO-first in first out(очередь в банк,выйдет первым тот кто был первым)

#LIFO- last in first out()



'========================методы set============================'


'add-добавляет элементы в set'
# set2={1,2,3}
# set2.add(3)#{1,2,3}
# set2.add(5)#{1,2,3,5}
# print(set2)

"pop удаляет случайный элемент  из set()"

# set2={1,2,3}
# popped=set2.pop()

# print(set2)
# print(popped)




'remove-удаляет элемент из set по значению'
set3={1,2,3}
# set3.remove(3)
# print(set3)


# print(dir(set))

"union обьеденяет обе два set"

# print(set1.union(set2))
#print(set1)


'update-обединяет set1 и set2 сохраняет изминения в set1'






"difference назодит разницу между set1 и set2"
# set1={1,2,3}
# set2={4,5,3}
# print(set2.difference(set1))#1,2
# print(set1.difference(set2))#{4,5}

"set1-set2"
# 'set2-set1'



'symmetric_difference'

# set1={1,2,3}
# set2={4,5,3}


# print(set1.symmetric_difference(set2))#{1,2,3,4}


"intersection (&) находиьь схожиие элементы из двух"
# set1={1,2,3,4}
# set2={4,3,5,6}
# print(set1.intersection(set2))#{3,4}
# print(set1&set2)#{3,4}






































































































