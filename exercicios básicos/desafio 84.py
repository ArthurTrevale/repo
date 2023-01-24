pessoa=[]
pessoas=[]
cadastrados=0
pesado=[]
leve=[]
while True:
    pessoa.append(input("Nome:"))
    pessoa.append(int(input("Peso:")))
    cadastrados+=1
    if pessoa[1]>=85:
        pesado.append(pessoa[:])
    elif pessoa[1]<=50:
        leve.append(pessoa[:])
    pessoas.append(pessoa[:])
    pessoa.clear()
    op=input("quer continuar?")
    if op == "n":
        break
print(pessoas)
print(f"quantidade de pessoas cadastradas: {cadastrados}")
print("os mais pessados são:",pesado)
print(f"os mais leves foram: {leve}")