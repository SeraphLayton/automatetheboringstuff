# 'apples, bananas, tofu, and cats' ( str with , and an "and" before last)

spam = []

def comcode (list):
    if list == []:
        return "empty"
    else :
        c = 1
        for i in range (len(spam)-1):
            list.insert(c, ",")
            c += 2
        list.insert(-1, "and")
        str1 = " "
        return str((str1.join(list)))

print(comcode(spam))
