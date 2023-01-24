class cpf:
    def __init__(self) -> None:
        self.h=input("Cpf:").replace('.','').replace('-','')
        h_soma_dig1=h_soma_dig2=h_som2=h_verif=h_verif2=0
        contador=10
        contador2=11
        noob=""
        try:
            int(self.h)
            noob="Sim"
        except ValueError:
            print("Digite apenas numeros")
            noob="Não"
        if noob=="Sim":
            if len(self.h)!=11:
                print("Erro, verifique se digitou certo!")
            else:
                for c in range (0,9,1):
                    h_soma_dig1+=(int(self.h[c])*contador)
                    h_soma_dig2+=(int(self.h[c])*contador2)
                    contador2-=1
                    contador-=1
        else:
            print()
        h_soma_dig2+=int(self.h[9])*2
        h_som2=(int(self.h[9])+int(self.h[10]))
        h_div=(h_soma_dig1*10)%11
        h_div2=(h_soma_dig2*10)%11
        h_verif+=int(self.h[9])
        h_verif2+=int(self.h[10])
        #70385063407
        if h_div == 10:
            h_div=0
        if h_div==h_verif and h_div2==h_verif2:
            print("valido")
        else:
            print("invalido")
