import re

passCheckRegex = re.compile(r'^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{8,})\S$')

password1 = input()

def passdetec(passw):
    if (passCheckRegex.search(passw) == None) is True:
        print("password is weak")
        return False
    else:
        print("password is strong")
        return True



passdetec(password1)

# Regex: ^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{8,})\S$
