import random
from re import T
filds=['python','c','java','c#','php','c++','javascript']
fild=random.choice(filds)
fild=list(fild)
true_chars=['_']*len(fild)
print(true_chars)
scors=len(fild)
while True:
    char=input('enter a fild :')
    for i in range(len(fild)):
        if fild[i]==char:
            true_chars[i]=char
    if char not in fild:
        scors-=1
    print(true_chars)
    if fild==true_chars:
        print('you win')
        break
    if scors==0:
        print('you lose')
        break
