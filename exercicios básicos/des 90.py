dic_inf={}
list_inf=[]
for c in range(0,2,1):
    dic_inf['Nome']=str(input("Nome:"))
    mmm=dic_inf['Media']=float(input("Média:"))
    if mmm<=6.9:
        dic_inf['situ']=str("Reprovado!")
    else:
        dic_inf['situ']=str("aprovado")
    list_inf.append(dic_inf.copy())
kij=""
count=0
for b in list_inf:
    for m,k in b.items():
        if count==0:
            kij="Nome="
            print(kij,k,end=' ')
            count+=1
        elif count==1:
            kij="Nota="
            print(kij,k,end=' ')
            count+=1
        else :
            kij="situação="
            print(kij,k,end=' ')
            count-=2
    print()
print(dic_inf)
print(list_inf)