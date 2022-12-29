# By ConfusedCharacter
# GitHub https://github.com/ConfusedCharacter/Password-Generator

import json
from itertools import chain, combinations
print("\n\t| Password Generator |\n\nNote: This Passwords are good for cracking.\n")

dic = json.loads(open("dic.json").read())

def powerset(iterable):
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def gen(word):
    words = []
    words.append(word.lower())
    words.append(word.upper())
    words.append(word.capitalize())
    value = ""
    for y,z in dic.items():
        value += (y)
    
    for i in powerset(value):
        text = word
        for a in i:
            text = text.lower().replace(a,dic[a])

        words.append(text)
        words.append(text.lower())
        words.append(text.upper())


    return "\n".join(set(words))


while True:
    name = input("[+] Enter Word : ")
    for x in name.split(","):
        data = gen(x)
        print(data)
        open("passwords-saved.txt",'a').write(data+"\n")