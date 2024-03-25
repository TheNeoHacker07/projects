list_=[1,2,3,4,5,6]
def func(a):
    if a>0:
        return True
    else:
        return False


result=list(map(func,list_))
print(result)