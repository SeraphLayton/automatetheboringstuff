import re

dateCheckRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})$')
# realDateCheckRegex = re.compile(r' ^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$ ')


date1 = "27/22/2000"
mo = dateCheckRegex.search(date1)

year = int(mo.group(3))
month = int(mo.group(2))
day = int(mo.group(1))

tomonths = [ '1', '3', '5', '7', '8', '10', '12' ]


def leapFeb():
    if year % 400 == 0 and year % 100 == 0:
        if month == 2 and day > 29:
            return False
        else:
            return True
    elif year % 4 == 0 and year % 100 != 0:
        if month == 2 and day > 29:
            return False
        else:
            return True
    else:
        if month == 2 and day <= 28:
            return True
    if month != 2:
        return True


def thirtyOne():
    if day > 31:
        return False
    if day == 31:
        if str(month) not in tomonths:
            return False
        else:
            return True
    else:
        return True



def dateVal(adate):
    if year < 1000 or year > 2999:
        return False
    if month < 1 or month > 12:
        return False
    if leapFeb() is False:
        print("Febuary")
        return False
    if thirtyOne() is False:
        print("31")
        return False
    return True
    
    

print(bool(dateVal(date1)))
