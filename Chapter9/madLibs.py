import re 
import pyinputplus as pyip 

#The results should be printed to the screen and saved to a new text file

testFile = open('./test1.txt')

text = testFile.read()
testFile.close()

finder = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

try: 
    for i in finder.findall(text):

        print("Enter a(n) " + i.lower() + ": ")
        newWord = pyip.inputStr(blockRegexes=[r'.*'], allowRegexes=[r'[^\W\d_]'])
        text = finder.sub(newWord, text, 1)
        final = finder.search(text)
    print(text)


    print("Name ur file: ")
    fName = input()
    fName = fName + '.txt'
    f = open(fName, 'w')
    f.write(text)

except KeyboardInterrupt:
    pass