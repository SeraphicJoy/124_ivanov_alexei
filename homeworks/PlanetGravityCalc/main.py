G=6.6743*10**(-11) #Gravitational Constant
m1=float(input("Insert 1st planet mass (without power of 10):"))*10**float(input("Insert power of 10:"))
m2=float(input("Insert 2nd planet mass (without power of 10):"))*10**float(input("Insert power of 10:"))
R=float(input("Insert distance between planets (in km):"))*1000 #Converts kilometres to metres
if m1>0 and m2>0 and R>0:
    F=G*m1*m2/R**2
print(F)