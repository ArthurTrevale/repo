from datetime import *
from datetime import date
def voto(a=0):
    data=date.today()
    ano= data.strftime("%Y")
    valor = int(ano)-a
    if valor<18 and valor>15 or valor>=65:
        print(f"idade: {valor} voto opcional")
    if valor >=18 and valor <=64:
        print(f"{valor} obrigatorio")
    if valor<=15:
        print(f"{valor} não vota")

cara=int(input("Ano:"))
voto(cara)