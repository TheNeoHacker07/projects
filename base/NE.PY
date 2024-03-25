# list1=[12,True,None,'hi',0,False,'makers','wolrd']


# list2=[i for i in list1 if type(i)==str]
# print(list2)




# dict1={'a':1,'b':2,'c':3}
# dic2={j:i for i,j in dict1.items()}
# print(dic2)



#ict1='a':[1,2,3],
#        'b':[12,0,1],
#        'c':[32,0,0,10]
     
# }

# dict2={i:sum(j) for i,j in dict1.items()}
# print(dict2)

# set1={1,12,'23',34,'makers'}
# set2={int(i) if i.isdigit() else i for i in set1}
# print(set2)

# dict1={1:[1],
#        2:[1,2],
#        3:[1,2,3],
#        4:[1,2,3,4],
#        5:[1,2,3,4,5]

#      }


# dict2={i:[i for i in range(1,6)] for i in range(1:6)}


# set_1={12,4,34,5,6}


# try:
#     num=int(input())
#     if num>0:
#         raise ValueError
#     elif num<0:
#          raise TypeError
#     else:
#          raise ZeroDivisionError
# except ValueError:
#     print('1')
# except TypeError:
#     print("-1")
# except ZeroDivisionError:
#     print('0'


# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

# list_=[ k.upper():v for k,v in dict_.items() if v in range(200,5000)]
# print(list_)