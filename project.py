from tkinter import *
import pyodbc
import pandas as pd
import openpyxl
from tkinter import ttk
from collections import defaultdict

#criando o software que vai injetar os dados no banco
jan= Tk()

#passando os dados de conexão
dados_conexao = ("Driver={SQL Server Native Client 11.0};"
                 "Server=DESKTOP-TMC67QR\SQLEXPRESS;"
                 "Database=Banco_1;"
                 "Trusted_Connection=yes"
                )

#conectando ao banco 
conexao = pyodbc.connect(dados_conexao)

#criando o "cursor"
cursor = conexao.cursor()

##tabelas
tabela_produto= pd.read_excel("tabelas\TABELA DIMENSÃO PATOS.xlsx")
tabela_geral= pd.read_excel("tabelas\TABELA FATOS.xlsx")
print(tabela_produto)
print(tabela_geral)

#editando o software

jan.title("protótipo")
jan.geometry("800x440")
jan.call("wm", "iconphoto",jan._w, PhotoImage(file="pngs\icone.ico"))
jan.wm_resizable(width=False, height=False)
jan.config(background="#FFA07A")

#criando os Entrys
produtosL=Label(text="Produto").place(x=15,y=25,height=22,width=120)
produto=Entry(jan,background="#5F9EA0")
produto.place(x=15,y=50,height=22,width=120)

preçoL=Label(text="Preço").place(x=15,y=75,height=22,width=120)
preço=Entry(jan,background="#5F9EA0")
preço.place(x=15,y=100,height=22,width=120)

quantiaL=Label(text="Quantia").place(x=15,y=125,height=22,width=120)
quantia=Entry(jan,background="#5F9EA0")
quantia.place(x=15,y=150,height=22,width=120)

idnL=Label(text="id").place(x=155,y=25,height=22,width=120)
idn=Entry(jan,background="#5F9EA0")
idn.place(x=155,y=50,height=22,width=120)

compradorL=Label(text="comprador").place(x=155,y=75,height=22,width=120)
comprador=Entry(jan,background="#5F9EA0")
comprador.place(x=155,y=100,height=22,width=120)

#for li in range(30):
    #Button(frame_2,text=f"aaaaaa{li}").grid(row=li,column=0,pady=10,padx=10)
frame_1=Frame(jan,height=450,width=200)
frame_1.place(x=360,y=20)

canvas_1 = Canvas(frame_1)
canvas_1.pack(side=LEFT,fill=BOTH,expand=1)

scroll_1 = ttk.Scrollbar(frame_1, orient= VERTICAL, command=canvas_1.yview)
scroll_1.pack(side=LEFT,fill=BOTH,expand=1)

canvas_1.configure(yscrollcommand=scroll_1.set)
canvas_1.bind('<Configure>', lambda e:canvas_1.configure(scrollregion=canvas_1.bbox("all")))

frame_2=Frame(canvas_1)

canvas_1.create_window((0,0),window=frame_2,anchor="nw")

def inject_b():
    v0=produto.get()
    v1=preço.get().replace(',','.')
    v1.replace('.',',')
    v2=quantia.get()
    v3=idn.get()
    v4=comprador.get()
    v5=int(quantia.get())*float(preço.get().replace(',','.'))
    comando = f"""INSERT INTO Dados (produto,preço,quantia,id,comprador,total)
                    VALUES 
                        ('{v0}','{v1}','{v2}','{v3}','{v4}','{v5}')"""

    cursor.execute(comando)
    cursor.commit()

botao_1=Button(text="Injetar Dados",background="cyan",command=inject_b)
botao_1.place(x=80,y=200,height=22,width=120)

def buscar():
    cursor.execute("select * from Dados;")
    linhas=cursor.fetchall()
    r=0
    frame_1=Frame(jan,height=450,width=200)
    frame_1.place(x=360,y=20)

    canvas_1 = Canvas(frame_1)
    canvas_1.pack(side=LEFT,fill=BOTH,expand=1)

    scroll_1 = ttk.Scrollbar(frame_1, orient= VERTICAL, command=canvas_1.yview)
    scroll_1.pack(side=LEFT,fill=BOTH,expand=1)

    canvas_1.configure(yscrollcommand=scroll_1.set)
    canvas_1.bind('<Configure>', lambda e:canvas_1.configure(scrollregion=canvas_1.bbox("all")))

    frame_2=Frame(canvas_1)

    canvas_1.create_window((0,0),window=frame_2,anchor="nw")

    for linha in linhas:
        b=f"produto: {linha[0]}\npreço: {linha[1]}\nquantia: {linha[2]} id: {linha[3]} comprador: {linha[4]}\ntotal: {linha[5]}"
        a=Label(frame_2,background="grey",text=b)
        a.grid(row=r,column=0,padx=10,pady=10)
        r+=6


botao_2=Button(text="buscar Dados",background="cyan",command=buscar)
botao_2.place(x=80,y=230,height=22,width=120)

def plan():
    cursor.execute("select * from Dados;")
    linhas=cursor.fetchall()
    dici=defaultdict(list)
    dici2=defaultdict(list)
    for linha in linhas:
        if linha[0]!="pato":
            dici['produto'].append(linha[0])
            dici['preço'].append(linha[1])
            dici['quantia'].append(linha[2])
            dici['id'].append(linha[3])
            dici['comprador'].append(linha[4])
            dici['total'].append(linha[5])
        else:
            dici['produto'].append(linha[0])
            dici['preço'].append(linha[1])
            dici['quantia'].append(linha[2])
            dici['id'].append(linha[3])
            dici['comprador'].append(linha[4])
            dici['total'].append(linha[5])

            dici2['produto'].append(linha[0])
            dici2['preço'].append(linha[1])
            dici2['quantia'].append(linha[2])
            dici2['id'].append(linha[3])
            dici2['comprador'].append(linha[4])
            dici2['total'].append(linha[5])

    plani=pd.DataFrame(dici)
    plani.to_excel("tabelas\TABELA FATOS.xlsx")
    plani2=pd.DataFrame(dici2)
    plani2.to_excel("tabelas\TABELA DIMENSÃO PATOS.xlsx")

botao_3=Button(text="Planilha",background="cyan",command=plan)
botao_3.place(x=80,y=260,height=22,width=120)

jan.mainloop()