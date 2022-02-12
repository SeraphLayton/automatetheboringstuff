import sys

def collatz(number):
    global eing
    if number % 2 == 0:
        number = number//2
        #print(number)
        eing = number
        return number
    elif number % 2 ==1:
        number = 3*number+1
       # print(number)
        eing = number
        return number

print("Youre Input: ")
eing=input()
try:
    eing=int(eing)
except ValueError:
    print("gimme number")
    sys.exit()


while True:
    if collatz(eing) != 1:
        print(eing)
    else:
        print("1")
        break