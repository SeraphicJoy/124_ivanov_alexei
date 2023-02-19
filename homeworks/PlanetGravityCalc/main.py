import math
G=6.6743*10**(-11) #Gravitational Constant
m1=5.97600*math.pow(10,24) #Mass of Earth
m2=float(input("Insert 2nd planet mass (without power of 10):")) #Mass of 2nd planet in kg
m2*=math.pow(10,int(input("Insert power of 10:")))
R=float(input("Insert distance between planets (in km):"))*1000 #Converts kilometres to metres
if m1>0 and m2>0 and R>0:
    F=G*m1*m2/R**2
print(F)