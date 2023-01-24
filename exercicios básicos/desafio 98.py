from time import sleep
def contador(i,f,p):
    for c in range (1,11,1):
        if c<=9:
            print(f"{c},",end='')
        else:
            print(f"{c}",end='')
    print("\n","-"*20)
    for c in range (10,-1,-2):
        if c>=1:
            print(f"{c},",end='')
        else:
            print(f"{c}",end='')
    print("\n","-"*20)
    if p>0:
        for c in range (i,f+1,p):
            if c<=f-1:
                print(f"{c},",end='')
            else:
                print(f"{c}",end='')
        print("\n","-"*20)
    else:
        for c in range (i,f-1,p):
            if c>=f+1:
                print(f"{c},",end='')
            else:
               print(f"{c}",end='')
        print("\n","-"*20)
ii=int(input("Inicio:"))
ff=int(input("Fim:"))
pp=int(input("passo:"))
contador(ii,ff,pp)