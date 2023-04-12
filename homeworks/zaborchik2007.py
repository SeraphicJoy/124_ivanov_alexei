str=input("Введите текст: ")
str2= ""
for i in range(len(str)):
    if not i%2 and str[i]!=" ":
        str2= str2 + str[i].upper()
    elif str[i]!=" ":
        str2= str2 + str[i].lower()
    else:
        str2 = str2 + str[i]

print(str2)