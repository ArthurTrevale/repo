def notas(*n,sit=False,show_dici=False):
    """calculador de notas para um dicionario
        ::variavel n: recebe a quantia de notas deigitadas, 1 2 3 4 ele se adpta
        ::variavel sit: valor boleano paar mostrar ou nao a situacao da turma 
        ::variavel show_dici: valor boleno para ver o 'dicionario' em si
    """
    dici={'quantidade':0,'total':0,'media':0}
    n2=len(n)
    for c in range(n2):
        dici['total']+=n[c]
        dici['quantidade']+=1
    
    dici['media']=dici['total']/n2
    
    if dici['media']>=8:
        situ="Boa"
    if dici['media']<=7.9 and dici['media']>=5.0:
        situ="mais ou menos "
    if dici['media']<=4.9:
        situ="ruim"
    
    if show_dici==False and sit == True:
        print(f"total:{dici['total']}\nmedia:{dici['media']:.2f}\nSitu:{situ}\nQuantia de notas inseridas: {dici['quantidade']}")
    if show_dici==False and sit == False:
        print(f"total:{dici['total']}\nmedia:{dici['media']:.2f}\nQuantia de notas inseridas: {dici['quantidade']}")
    if show_dici == True:
        print(dici)
def notas_outro_modo(*n,sit=False):
    r={}
    r['quantia']=len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    r['media']=sum(n)/len(n)
    print(f"quantidade:{r['quantia']}\nmaior nota:{r['maior']}\nmenor nota:{r['menor']}\nmédia:{r['media']:.2f}")
notas_outro_modo(4,5,8,9,5,6,8,7,2,4,6,9,8,2,3,5,4,10,10,10,2,5,8,4,6,7)
help(notas)
