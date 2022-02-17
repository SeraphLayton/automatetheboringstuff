import glob, os
from pathlib import Path
import re

print("Submit a valid absolute Path: ")
gPath = Path(input())
os.chdir(gPath)
print("\n")



print("Type in a regular expression: (example: [^\W\d_] or ADJECTIVE|NOUN|ADVERB|VERB )")
uEx = input()
regex = re.compile(str(uEx))
print("\n")

for file in glob.glob("*.txt"):
    cFile = open(str(gPath) + '/' + file)
    print("Found following reg(" + uEx +") in " + file)
    for i in regex.findall(cFile.read()):
        print(i)
    print("\n")