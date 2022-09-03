x=[]
a=[]
for i in range(1,1000):
    n=int(input('enter your numbers?'))
    if n%2==0:
        print('true')
        x.append(n)
        a.append(n)
        print('x,a=',(x))
    if n%2:
        print('false')
    if n%2==0:       
        print('x=',len(x))
        print('a=',len(a))
