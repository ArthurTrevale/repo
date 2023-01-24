def fatorial(valor=0,mostrar=False):
    flag=0
    for c in range (1,valor):
        if mostrar==False:
            valor=valor*c
        else:
            valor=valor*c
            print(f"{c}x",end='')
            flag=1
        valor2=valor
    if flag==1:
        print(f"x{c+1}",end='')
        print("= ",end='')
    return valor2
numero=int(input("valor:"))
most=bool(input("não mostrar [não digite nada] para mostarr [digite qualquer coisa]:"))
print(fatorial(numero,most))