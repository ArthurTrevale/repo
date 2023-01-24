from random import *
from time import sleep
lt_p=[]
l_p=[]
l_p2=[]
nn=0
n_p=int(input("Quantos palpites:"))
for j in range (0,n_p,1):
    for b in range (0,6,1):
        nn=randint(1,60)
        #print(nn)
        if len(l_p)<=6:
            if nn in l_p:
                pass
            else:
                l_p.append(nn)
        else:
            pass
    lt_p.append(l_p[:])
    l_p2=l_p[:]
    l_p.clear()
for i in range  (0,n_p,1):
    print(f"{i+1}º Palpite{lt_p[i]}")
    sleep(0.8)