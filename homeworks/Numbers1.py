import random

def magic():
    list=[]
    for i in range(random.randint(50,100)):
        list.append(random.randint(0,9999))
    x=int(input("Enter a number: "))
    if len(list)%x==0:
        return True
    else:
        return False
print(magic())