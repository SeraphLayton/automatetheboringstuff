import pyinputplus as pyip 
import random
from time import sleep

numberOfQuestions = 10
correctAnswers = 0

try:
    for i in range(numberOfQuestions):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        response = pyip.inputInt(prompt="Question #"+str(i+1)+" \nWhat is "+str(num1) +"x"+str(num2)+"? \n"  , min=0, max=81, limit=3, timeout=8, default='N/A')
        if response == (num1 * num2):
            print("Correct!\n")
            correctAnswers += 1
            sleep(1)
        elif response == 'N/A':
            continue
        
    print("U got "+ str(correctAnswers) +" answers right!")
except KeyboardInterrupt:
    print('KeyboardInterrupt exception is caught')