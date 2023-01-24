from time import sleep
def leiaint(num=''):
    """
    funcao e para verificar se e inteiro 
    :parametro num = recebe o suposto valor inteiro 
    """ 
    while True:
        if num == "":
            num=input("Nada não é um valor:")
        no = num.find("-")
        no2 = num.count("-")
        if " " in num:
            num=num.replace(" ","")
        if "-" in num and no==0 and no2==1:
            negativo=True
        else:
            negativo=False
        
        if negativo==True:
            nume=num.strip().replace('-','')
            if nume.isnumeric():
                print(f"sim,-->[{num}]<-- é um valor valido")
                break
            else:
                num=input(f"erro,-->[{num}]<-- não é um valor valido\nvalor:")
        else:
            if num.isnumeric():
                print(f"sim,-->[{num}]<-- é um valor valido")
                break
            else:
                num=input(f"erro,-->[{num}]<-- não é um valor valido\nvalor:")

help(sleep)
help(leiaint)
jo=input("valor:")
leiaint(jo)
