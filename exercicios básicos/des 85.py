n=[]
p=[]
i=[]
for c in range(0,7,1):
    nu=(int(input("Valor:")))
    if nu%2==0:
        p.append(nu)
    else:
        i.append(nu)
    n.append(nu)
    n.sort()
n2=[]
n2.append(i)
n2.append(p)
print(f"Lista={n}\nPar={p}\nImpar={i}")
print(n2)