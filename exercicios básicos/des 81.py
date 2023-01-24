
listaA=[]
listaB=[]
listaC=[]
cod=''
c=0
t5="não foi"
while True:
    var=input("Valor:").replace(' ','')
    if var == "Stop":
        break
    else:
        if var != '':
            try:
                int(var)
            except ValueError:
                listaA.append(var)
            else:

                if var == 5 or var == "5":
                    t5 = "foi"
                c+=1
                listaB.append(var)
listaA.sort()
listaB.sort(reverse=True)
k=len(listaA+listaB)
for j in range (0,k,1):
    try:
        listaC.append(listaA[j])
        listaC.append(listaB[j])
        cod+= listaA[j]+listaB[j]
    except IndexError:
        pass
print(f"Contador: {c}\n Lista em valores decresscentes:{listaB}\nLista em ordem alfabetica:{listaA}\nO valor 5 foi digitado?: {t5}")
print(listaC)
print(f"Codigo:{cod}")