matriz=[[0]*3,[0]*3,[0]*3]
for c in range (0,3,1):
    for l in range (0,3,1):
        n=int(input(f"Valot da posição {c}|{l}:"))
        matriz[c][l]=n
for i in range (0,3,1):
    for b in range (0,3,1):
        print(f"[{matriz[i][b]}]",end="")
    print()