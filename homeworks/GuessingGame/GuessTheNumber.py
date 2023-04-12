import random

UserName=input("Введите имя пользователя: ")
ComputerNumber=random.randint(1,100)
print("Компьютер загадал число от 1 до 100. Угадайте это число.")
UserNumber=int(input("Введите число: "))
Tries=0
k=0
while k!=1:
    if UserNumber==ComputerNumber:
        Tries+=1
        print("Вы угадали загаданное число", ComputerNumber, "за", Tries, "попыток!")
        b="Имя пользователя: "+UserName+"\n"
        c="Количество попыток: "+str(Tries)
        f=open('game.txt', 'w')
        with f:
            f.write(b)
            f.write(c)
        k+=1
    elif UserNumber<1 or UserNumber>100:
        UserNumber=int(input("Ошибка. Введите число от 1 до 100: "))
    else:
        Tries+=1
        if UserNumber>ComputerNumber:
            print("Меньше.")
        else:
            print("Больше.")
        UserNumber = int(input("Введите число: "))


