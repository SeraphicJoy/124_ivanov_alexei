import re

def search_substr(subst,st):
    if re.search(subst, st, re.IGNORECASE):
        return "Есть контакт!"
    else:
        return "Мимо!"
st=input()
subst=input()
print(search_substr(subst, st))