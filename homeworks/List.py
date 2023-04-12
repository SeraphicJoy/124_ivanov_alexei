import random

List1=[]
List2=[]

for i in range(random.randint(50,100)):
    List1.append(random.randint(0,9999))

for i in range(random.randint(50,100)):
    List2.append(random.randint(0,9999))
result1=list(set(List1) - set(List2))
result2=list(set(List1) & set(List2))
print("Значения из 1 списка, которых нет во 2:", result1)
print("Общие значения из двух списков:", result2)