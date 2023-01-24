lista=[]
listaP=[]
listaI=[]
i=0
f=0
while True:
    x=input("Valor: ")
    if x=="Pare":
        break
    try:
        int(x)
    except ValueError:
        i=0
    else:
        i=1
    try:
        float(x)
    except ValueError:
        f=0
    else:
        f=1
    if i==1 and f==0:
        lista.append(x)
        if int(x)%2==0:
            listaP.append(x)
        else:
            listaI.append(x)
    if i==1 and f==1:
        lista.append(x)
        k=float(x)%2
        print(k)
        if k in (2,4,6,8):
            listaP.append(x)
        else:
            listaI.append(x)
print(lista,listaP,listaI)