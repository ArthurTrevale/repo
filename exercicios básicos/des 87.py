matriz=[[0]*3,[0]*3,[0]*3]
som_par=som_col_3=M_v=0
for c in range (0,3,1):
    for l in range (0,3,1):
        n=int(input(f"Valot da posição {c}|{l}:"))
        matriz[c][l]=n
        if n%2==0:
            som_par+=n
        if l==2:
            som_col_3+=n
        if c==1:
            if M_v<n:
                M_v=n
        else:
            pass
for i in range (0,3,1):
    for b in range (0,3,1):
        print(f"[{matriz[i][b]}]",end="")
    print()
print(f"Soma dos pares :{som_par}")
print(f"Soma da 3º coluna :{som_col_3}")
print(f"Maior valor da 2º linha :{M_v}")