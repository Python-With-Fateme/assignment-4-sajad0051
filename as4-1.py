n=int(input('chand ta mikhay vard koni?'))
for i in range(n):
        s=1
        a=int(input(f'enter your add{i+1}? '))
        for j in range(1,a+1):
            s=s*j
        print(s)