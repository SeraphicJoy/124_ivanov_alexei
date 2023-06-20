vowels=('a','e','i','o','u')
string=input()
newstring=''
for i in range(len(string)):
    if string[i] not in vowels:
        newstring+=string[i]
print(newstring)
