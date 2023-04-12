import random

N=int(input("Количество моментов времени: "))
S=[]
D=[]
counter=0
for i in range(N):
    S.append(random.randint(0,100))
for i in range(N):
    D.append(random.randint(0,100))
for i in range(len(S)):
    if S[i]==D[i]:
        counter+=1
print("Количество моментов рыночного равновесия:", counter)
