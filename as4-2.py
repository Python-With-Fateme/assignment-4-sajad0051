n=int(input('enter yor add?'))
b=[]
while len(b)!=n:
    m=float(input('enter your number? '))
    if m%2==0:
        b.append(m)
    print(b)