def ficha(jo="",go=0):
    if jo=="":
        print(f"o jogador <Vazio> fez {go} gol(s)")
    else:
        print(f"o jogador <{jo}> fez {go} gol(s)")
jogador=input("Jogador:")
try:
    gols=int(input("Gols:"))
except ValueError:
    gols=0
ficha(jogador,gols)
ficha("noznoz",105)