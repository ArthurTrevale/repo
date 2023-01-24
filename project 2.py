from time import sleep
from tkinter import *
import babel.numbers #NESCESSARIO PRA O EXECUTAVEL RODAR
import webbrowser
import pyodbc
from tkinter import ttk
import tkinter as tk
import pygame
import socket #TBM NECESSARIO, APENAS DE N USAR LITERALMENTE
import chat_cliente
from tkinter import filedialog
from tkinter import messagebox
new = 2

class Pessoa:
    def __init__(self) -> None:
        self.nome
class Convidado(Pessoa):
    def __init__(self) -> None:
        super().__init__()
class Aluno(Pessoa):
    def __init__(self) -> None:
        super().__init__()
        self.login
        self.senha
class Professor(Aluno):
    def __init__(self) -> None:
        super().__init__()
class Funcionario(Aluno):
    def __init__(self) -> None:
        super().__init__()

volume=0.5
is_on=True
contador=0
####HTMLS######

url = "https://www.ultrafarma.com.br/categoria/medicamentos/hormonios-e-enzimas/anabolizantes"
url2 = "https://www.gsuplementos.com.br/"
url3 = "https://www.boletobancario.com/boletoservice/servlet/BoletoService?test=true&clientId=11222333444455&clientPass=senhateste&nossoNumero=378&numDoc=GC+8289&valor=120%2C00&vencimento=07%2F06%2F2022&numeroBanco=237&agencia=1234&codBeneficiario=5678&carteira=02&nomePagador=ID_user_expected&enderecoPagador=Rua+do+nunca+nem+vi&cepPagador=12345-678&cidadePagador=Natal&estadoPagador=Rio+Grande+do+Norte&infoAdicionais=&mensagem1=Fatura+referente+aos+servicos+prestados&mensagem2=Apos+o+vencimento+acesse+nosso+site+para+gerar+uma+nova+fatura&mensagem3=LOCBOY+ACADEMY.LTDA&mensagem4=Todos+os+direitos+reservados&mensagem5=&mensagem6=&mensagem7=&mensagem8=www.LocBoy_Academy.com.br&format=html"

############FUNÇÕES GLOBAIS//CLASSE FUNÇÕES############
class Func():
    # conexão com o banco
    dados_conexao = ("Driver= {ODBC Driver 17 for SQL Server};"
                    "Server=LAPTOP-ACD473OO;"
                    "Database=academia_projeto;"
                    "Trusted_Connection=yes"
                    )
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    def cor_botao(botao, color1, color0):
        botao.bind("<Enter>", func=lambda e: botao.config(
            background=color1))
        botao.bind("<Leave>", func=lambda e: botao.config(
            background=color0))



#############inicializando o pygamer mixer#######################
    pygame.mixer.init()
#############FUNÇÃO (botão da musica)#######################
    def vol_som():
        global volume
        if volume<1.00:
            volume+=0.02
            pygame.mixer.music.set_volume(volume)
            txt_som_la=Label(text=f"{volume*100:.2f}",bg="#20B2AA",foreground="#FFFF00",font=('',18))
            txt_som_la.place(relx=0.0,rely=0.1,relheight=0.08,relwidth=0.15)
            txt_som_la.after(1000,txt_som_la.destroy)
        else:
            pass
    def vol_sub():
        global volume
        if volume>0.02:
            volume-=0.02
            pygame.mixer.music.set_volume(volume)
            txt_som_la=Label(text=f"{volume*100:.2f}",bg="#20B2AA",foreground="#FFFF00",font=('',20))
            txt_som_la.place(relx=0.0,rely=0.1,relheight=0.08,relwidth=0.15)
            txt_som_la.after(1000,txt_som_la.destroy)
        elif volume<=0.02:
            volume=0
            pygame.mixer.music.set_volume(volume)
            txt_som_la=Label(text=f"{volume*100:.2f}",bg="#20B2AA",foreground="#FFFF00",font=('',20))
            txt_som_la.place(relx=0.0,rely=0.1,relheight=0.08,relwidth=0.10)
            txt_som_la.after(1000,txt_som_la.destroy)
        else:
            pass
    def play():
        global volume
        pygame.mixer.music.load("pngs\ledson.mp3")
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops=0)

    def play2():
        global volume
        pygame.mixer.music.load("pngs\Mag_Quer_Tomar_Bomba.mp3")
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops=999999)


class Tela_Login:
    Func.play2()
    def __init__(self) -> None:
        # conexão com o banco
        dados_conexao = ("Driver= {ODBC Driver 17 for SQL Server};"
                        "Server=LAPTOP-ACD473OO;"
                        "Database=academia_projeto;"
                        "Trusted_Connection=yes"
                        )
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
        
        ######FUNÇÕES########
        def botao_registrar():
            self.jan.destroy()
            Tela_Registro()
        def botao_log():
            consultar = "select * from  Info_Usua"
            cursor = conexao.cursor()
            cursor.execute(consultar)
            linhas = cursor.fetchall()
            consultar2= "select * from  Info_Funcino"
            cursor2=conexao.cursor()
            cursor2.execute(consultar2)
            linhas2= cursor2.fetchall()
    
######### verificando se não é um espaço vazio ###############
            valid="a"
            valid2="b"
            if slot_login.get() != "" and slot_senha.get() != "" :
                login = slot_login.get()
                slot_login.delete(0, END)
                senha = slot_senha.get()
                slot_senha.delete(0, END)
            else:
                txt_falha_vazio = Label(self.jan, text="Digite\n o login e a senha", font=("Negrito", 10), bg="Red")
                txt_falha_vazio.place(relx=0.71, rely=0.47, relheight=0.10, relwidth=0.15)
                txt_falha_vazio.after(1250,txt_falha_vazio.destroy)
###################### verificando se o login está correto!(alocado no banco de dados)##############
            if login== "visita" and login== "visita":
                self.jan.destroy()
                Tela_Sucesso_Login()
            for l in linhas:
                if l[1] == login and l[2] == senha:
                    valid="aluno"
                    break
                else:
                    txt_falha = Label(self.jan, text="Usuario ou senha\ninvalidos!", font=("Negrito", 10), bg="Red")
                    txt_falha.place(relx=0.71, rely=0.47, relheight=0.10, relwidth=0.15)
                    txt_falha.after(1250,txt_falha.destroy)
            for l in linhas2:
                if l[1] == login and l[2] == senha:
                    valid2="funcionario"
                    break
                else:
                    txt_falha = Label(self.jan, text="Usuario ou senha\ninvalidos!", font=("Negrito", 10), bg="Red")
                    txt_falha.place(relx=0.71, rely=0.47, relheight=0.10, relwidth=0.15)
                    txt_falha.after(1250,txt_falha.destroy)
            if valid == "aluno" or valid2== "funcionario":
                self.jan.destroy()
                Tela_Sucesso_Login()
            else:
                txt_falha = Label(self.jan, text="Usuario ou senha\ninvalidos!", font=("Negrito", 10), bg="Red")
                txt_falha.place(relx=0.71, rely=0.47, relheight=0.10, relwidth=0.15)
                txt_falha.after(1250,txt_falha.destroy)
        def play2_para():
            global contador
            if contador%2==0:
                pygame.mixer.music.stop()
                contador+=1
            else:
                pygame.mixer.music.load("pngs\Mag_Quer_Tomar_Bomba.mp3")
                pygame.mixer.music.play(loops=999999)
                contador+=1

        #config/janela
        self.jan = Tk()
        self.jan.call("wm", "iconphoto", self.jan._w, PhotoImage(file="pngs\icone.ico"))
        
        # imagens usadas:
        img = PhotoImage(file="pngs\llogo_teste12.png").subsample(2, 2)
        Label_img = Label(self.jan, image=img, background="#20B2AA").place(relx=0.35, rely=0.08,relheight=0.20, relwidth=0.25)

        # titulo
        self.jan.title("LOCBOY Academy")

        # cor fundo
        self.jan.config(bg="#20B2AA")

        # size
        self.jan.geometry("480x360")

        # textos na interface
        txt_log = Label(self.jan, text="Usuário:")
        txt_log.place(relx=0.26, rely=0.45, relheight=0.066, relwidth=0.10)
        txt_sen = Label(self.jan, text="Senha:")
        txt_sen.place(relx=0.26, rely=0.55, relheight=0.066, relwidth=0.10)

        # login
        slot_login = Entry()
        slot_login.place(relx=0.38, rely=0.45, relheight=0.066, relwidth=0.30)

        # senha
        slot_senha = Entry(self.jan, show="*")
        slot_senha.place(relx=0.38, rely=0.55, relheight=0.066, relwidth=0.30)

        # botoes
        but_log = Button(self.jan, text="Logar",command=botao_log)
        but_log.place(relx=0.30, rely=0.67, relheight=0.066, relwidth=0.11)

        but_reg = Button(self.jan, text="Registre-se",command=botao_registrar)
        but_reg.place(relx=0.50, rely=0.67, relheight=0.066, relwidth=0.16)

        img_mag=PhotoImage(file="pngs\images.png")

        imgbb=PhotoImage(file="pngs\labobora.png").subsample(5,5)
        but_music = Button(self.jan,image=imgbb,command=lambda:[play2_para()])
        but_music.place(relx=0.00, rely=0.00, relheight=0.06, relwidth=0.06)
        but_music_volu = Button(self.jan,text="+",command=Func.vol_som)
        but_music_volu.place(relx=0.09, rely=0.00, relheight=0.03, relwidth=0.03)
        but_music_volu2 = Button(self.jan,text="-",command=Func.vol_sub)
        but_music_volu2.place(relx=0.12, rely=0.00, relheight=0.03, relwidth=0.03)

        txt_log_visita = Label(self.jan, text="visitante\nlogin:visita\nsenha:visita")
        txt_log_visita.place(relx=0.10, rely=0.45, relheight=0.166, relwidth=0.15)
        # fontes
        txt_log.config(font=("Segoe Script", 8))
        txt_sen.config(font=("Segoe Script", 8))

        but_log.config(font=("", 12))
        but_reg.config(font=("", 11))

        # cor slots e botoes textos
        slot_login.config(bg="#4682B4", foreground="#FFFF00")
        slot_senha.config(bg="#4682B4", foreground="#FFFF00")

        but_log.config(bg="#00FA9A", fg="#000080")
        but_reg.config(bg="#00FF00", fg="Black")
        # fim
        self.jan.mainloop()
        


class Tela_Registro():
    def __init__(self) -> None:
            # conexão com o banco
        dados_conexao = ("Driver= {ODBC Driver 17 for SQL Server};"
                        "Server=LAPTOP-ACD473OO;"
                        "Database=academia_projeto;"
                        "Trusted_Connection=yes"
                        )
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
        ######Validações#####
        valid_cpf=0
        valid_email=0
        ######FUNÇÕES########
        def retornar():
            self.jan.destroy()
            Tela_Login()
        def pegar():
            #verificar se preencheu tudo
            if slot_reg_name.get() != '' and slot_reg_log.get() != '' and slot_reg_sen.get()!= '' and slot_reg_email.get() != '' and slot_reg_data.get() != '' and slot_reg_sexo.get() != '' and slot_reg_cpf.get() != '' and slot_reg_plan.get() != '':
                h =slot_reg_cpf.get().replace('.','').replace('-','')
                h_soma_dig1=h_soma_dig2=h_som2=h_verif=h_verif2=0
                contador=10
                contador2=11
                #tratar erros
                try:
                    int(h)
                except ValueError:
                    cpf_error=Label(self.jan,text="não sabia que cpf agora tinha letras em sua composição",bg="red")
                    cpf_error.place(relx=0.55,rely=0.18)
                    cpf_error.after(2500,cpf_error.destroy)

                if len(h)!=11:
                    cpf_error=Label(self.jan,text="um cpf possui 11 digitos númericos, sem contar com . e - ",bg="red")
                    cpf_error.place(relx=0.55,rely=0.06)
                    cpf_error.after(2500,cpf_error.destroy)
                else:
                    #calulo de verificação
                    for c in range (0,9,1):
                        h_soma_dig1+=(int(h[c])*contador)
                        h_soma_dig2+=(int(h[c])*contador2)
                        contador2-=1
                        contador-=1
                h_soma_dig2+=int(h[9])*2
                h_som2=(int(h[9])+int(h[10]))
                h_div=(h_soma_dig1*10)%11
                h_div2=(h_soma_dig2*10)%11
                h_verif+=int(h[9])
                h_verif2+=int(h[10])
                if h_div == 10:
                    h_div=0
                if h_div==h_verif and h_div2==h_verif2:
                    valid_cpf=15
                else:
                    cpf_error=Label(self.jan,text="cpf invalido!",bg="red")
                    cpf_error.place(relx=0.6,rely=0.14)
                    cpf_error.after(2500,cpf_error.destroy)
                idade= slot_reg_data.get()
                try:
                    int(idade) 
                except ValueError:
                    data_error=Label(self.frame1,text="não sabia que idades agora tinham letras em sua composição",bg="red")
                    data_error.place(relx=0.054, rely=0.356, relheight=0.05, relwidth=0.55)
                    data_error.after(2500,data_error.destroy)
                else:
                    if int(idade)<100 and int(idade)>0 :
                            data_valid = 125
                    else:
                        if int(idade)>=100:
                            data_error=Label(self.frame1,text="não aceitamos velhotes de 100 ou mais",bg="red")
                            data_error.place(relx=0.054, rely=0.356, relheight=0.15, relwidth=0.55)
                            data_error.after(2500,data_error.destroy)
                        if int(idade)<=0:
                            data_error=Label(self.frame1,text="é um deus supremo, veio à min antes mesmo\n de nascer",bg="red")
                            data_error.place(relx=0.054, rely=0.356, relheight=0.15, relwidth=0.55)
                            data_error.after(2500,data_error.destroy)                
                #validação e-mail
                if not'@' in slot_reg_email.get():
                    email_error=Label(self.jan,text="Isso não é um e-mail, um e-mail tem um @",bg="Red")
                    email_error.place(x=130, y=253.3)
                    email_error.after(2500,email_error.destroy)
                else:
                    try:
                        slot_reg_email.get().index('.')
            
                    except ValueError:
                        email_error=Label(self.jan,text="um e-mail,é composto por um .com e um exemple antes dele\nexemplo: nome@example.com",bg="Red")
                        email_error.place(x=130, y=253.3)
                        email_error.after(2500,email_error.destroy)
                    va=slot_reg_email.get().find('@')
                    vb=slot_reg_email.get().index('.')
                    if vb != va+1:
                        if not ".com" in slot_reg_email.get():
                            email_error=Label(self.jan,text="um e-mail,é composto por um .com e um exemple antes dele\nexemplo: nome@example.com",bg="Red")
                            email_error.place(x=130, y=253.3)
                            email_error.after(2500,email_error.destroy)
                        else:
                            valid_email=32
                    else:
                        email_error=Label(self.jan,text="um e-mail,é composto por um . mas ele não é ai e um exemple antes dele\nexemplo: nome@example.com",bg="Red")
                        email_error.place(x=130, y=253.3)
                        email_error.after(2500,email_error.destroy)
                if valid_cpf==15 and valid_email==32:
                    reg_nome = slot_reg_name.get()
                    reg_login = slot_reg_log.get()
                    reg_senha = slot_reg_sen.get()
                    reg_email = slot_reg_email.get()
                    reg_data = slot_reg_data.get()
                    reg_sexo = slot_reg_sexo.get()
                    reg_cpf = slot_reg_cpf.get()
                    reg_plan = slot_reg_plan.get()
                    # comando
                    comando = f"""INSERT INTO Info_Usua (nome,cpf,login,senha,email,plano,sexo,data)
                    VALUES 
                        ('{reg_nome}','{reg_cpf}','{reg_login}','{reg_senha}','{reg_email}','{reg_plan}','{reg_sexo}','{reg_data}')"""
                    cursor.execute(comando)
                    cursor.commit()
                    # apagar
                    slot_reg_name.delete(0, END)
                    slot_reg_log.delete(0, END)
                    slot_reg_sen.delete(0, END)
                    slot_reg_email.delete(0, END)
                    slot_reg_data.delete(0, END)
                    slot_reg_sexo.delete(0, END)
                    slot_reg_cpf.delete(0, END)
                    slot_reg_plan.delete(0, END)
                else:
                    cpf_error=Label(self.jan,text="alguma informação está errada!",bg="red")
                    cpf_error.place(relx=0.8,rely=0.15)
                    cpf_error.after(2500,cpf_error.destroy)
            else:
                campos_erro_txt=Label(self.jan,text="Preencha\n todos\n os\n campos!",height=10,width=20,bg="red")
                campos_erro_txt.place(relx=0.40,rely=0.40)
                campos_erro_txt.after(1500,campos_erro_txt.destroy)
        
########################config
        self.jan = Tk()
        self.jan.call("wm", "iconphoto", self.jan._w, PhotoImage(file="pngs\icone.ico"))
        self.jan.wm_resizable(width=False, height=False)
        self.jan.config(bg="#87CEEB")
        self.jan.geometry("760x560")
        self.jan.title("Registre-se")
################# listas
        sexo_list = ["Masculino", "Feminino", "Trans", "Binario", "Helicoptero de Combate",
                    "Geladeira Eletrolux Três Portas", "Megazord", "Outro"]
        plano_list =["Básico – R$ 70.00", "Médio - R$ 90.00", "Completo – R$ 120.00"]

######################### slots
        slot_reg_name = Entry(self.jan)  # nome
        slot_reg_name.place(x=30, y=73.3, height=25, width=300)

        slot_reg_cpf = Entry(self.jan)  # cpf
        slot_reg_cpf.place(x=380, y=73.3, height=25, width=300)

        slot_reg_log = Entry(self.jan)  # login
        slot_reg_log.place(x=30, y=133.3, height=25, width=300)

        slot_reg_plan = ttk.Combobox(self.jan,values=plano_list,state="readonly")  # plano
        slot_reg_plan.place(x=380, y=133.3, height=25, width=300)

        slot_reg_sen = Entry(self.jan, show="*")  # senha
        slot_reg_sen.place(x=30, y=193.3, height=25, width=300)

        slot_reg_email = Entry(self.jan)  # e-mail
        slot_reg_email.place(x=30, y=253.3, height=25, width=300)

        slot_reg_data = Entry(self.jan)  # data de nascimento
        slot_reg_data.place(x=30, y=313.3, height=25, width=300)

        slot_reg_sexo = ttk.Combobox(self.jan, values=sexo_list)  # sexo
        slot_reg_sexo.place(x=30, y=373.3, height=25, width=300)

        # textos
        slot_reg_name_txt = Label(self.jan, text="Nome Completo",bg="#00FA9A")  # nome
        slot_reg_name_txt.place(x=30, y=53.3, height=25, width=300)
    
        slot_reg_cpf_txt = Label(self.jan, text="Cpf",bg="#00FA9A")  # cpf
        slot_reg_cpf_txt.place(x=380, y=53.3, height=25, width=300)

        slot_reg_log_txt = Label(self.jan, text="Criar Login")  # login
        slot_reg_log_txt.place(x=30, y=113.3, height=25, width=300)
        slot_reg_log_txt.config(bg="#00FA9A")

        slot_reg_plan_txt = Label(self.jan, text="Selecione um plano")  # plano
        slot_reg_plan_txt.place(x=380, y=113.3, height=25, width=300)
        slot_reg_plan_txt.config(bg="#00FA9A")

        slot_reg_sen_txt = Label(self.jan, text="Criar Senha")  # senha
        slot_reg_sen_txt.place(x=30, y=173.3, height=25, width=300)
        slot_reg_sen_txt.config(bg="#00FA9A")

        slot_reg_email_txt = Label(self.jan, text="E-mail")  # e-mail
        slot_reg_email_txt.place(x=30, y=233.3, height=25, width=300)
        slot_reg_email_txt.config(bg="#00FA9A")

        slot_reg_data_txt = Label(self.jan, text="idade")  # data de nascimento
        slot_reg_data_txt.place(x=30, y=293.3, height=25, width=300)
        slot_reg_data_txt.config(bg="#00FA9A")

        slot_reg_sexo_txt = Label(self.jan, text="Sexo")  # sexo
        slot_reg_sexo_txt.place(x=30, y=353.3, height=25, width=300)
        slot_reg_sexo_txt.config(bg="#00FA9A")

        # botão
        but_cad = Button(self.jan, text="Cadastrar", command=pegar, font=("", 12), bg="#98FB98")
        but_cad.place(x=143, y=423.3, height=35, width=80)
        but_retorno = Button(self.jan, text="Voltar", command=retornar, font=("", 12), bg="Red",foreground="Black")
        but_retorno.place(x=143, y=470.3, height=35, width=80)
        self.jan.mainloop()



class Tela_Sucesso_Login():
    def __init__(self) -> None:
        # conexão com o banco
        dados_conexao = ("Driver= {ODBC Driver 17 for SQL Server};"
                        "Server=LAPTOP-ACD473OO;"
                        "Database=academia_projeto;"
                        "Trusted_Connection=yes"
                        )
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
        #funções internas
        def foto():
            filedialog.askopenfilenames()
        def chat34():
            self.jan.destroy()
            chat_cliente.FirstScreen()
        self.jan = Tk()
        self.jan.call("wm", "iconphoto", self.jan._w, PhotoImage(file="pngs\icone.ico"))
        self.jan.title("LOCBOY ACADEMY")
        self.jan.geometry("670x670")
        self.jan.config(bg="#20B2AA")
        meumenu=Menu(self.jan)
        self.jan.config(menu=meumenu)

        img = PhotoImage(file="pngs\llogo_teste12.png").subsample(1, 1)
        Label_img = Label(self.jan, image=img, background="#20B2AA")
        Label_img.place(relx=0.33, rely=0.0,relheight=0.30,relwidth=0.40)

        def inserir():
            self.lb.destroy()
            self.tv.destroy()
            self.tv=ttk.Treeview(self.frame3,columns=("nome","login","senha","email","idade","sexo","cpf","plano"),show='headings')
            self.tv.column('nome',minwidth=0,width=50)
            self.tv.column('login',minwidth=0,width=50)
            self.tv.column('senha',minwidth=0,width=50)
            self.tv.column('email',minwidth=0,width=50)
            self.tv.column('idade',minwidth=0,width=50)
            self.tv.column('sexo',minwidth=0,width=50)
            self.tv.column('cpf',minwidth=0,width=50)
            self.tv.column('plano',minwidth=0,width=50)
            self.tv.heading('nome',text="nome")
            self.tv.heading('login',text="login")
            self.tv.heading('senha',text="senha")
            self.tv.heading('email',text="email")
            self.tv.heading('idade',text="idade")
            self.tv.heading('sexo',text="sexo")
            self.tv.heading('cpf',text="cpf")
            self.tv.heading('plano',text="plano")
            self.tv.place(relx=0.005,rely=0.02,relheight=0.80,relwidth=0.99)
            self.lb = Scrollbar(self.tv,orient="vertical",command=self.tv.yview)
            self.lb.pack(side=RIGHT,fill="y")
            self.tv.configure(yscrollcommand=self.lb.set)
            cursor7=conexao.cursor()
            cursor7.execute("SELECT * FROM Info_Usua")
            resultado=cursor7.fetchall()
            for x in resultado:
                self.tv.insert("","end",values=(tuple(x)))

        def inserir2():
            self.lb.destroy()
            self.tv.destroy()
            self.tv=ttk.Treeview(self.frame3,columns=("nome","login","senha","email","idade","sexo","cpf","salario"),show='headings')
            self.tv.column('nome',minwidth=0,width=50)
            self.tv.column('login',minwidth=0,width=50)
            self.tv.column('senha',minwidth=0,width=50)
            self.tv.column('email',minwidth=0,width=50)
            self.tv.column('idade',minwidth=0,width=50)
            self.tv.column('sexo',minwidth=0,width=50)
            self.tv.column('cpf',minwidth=0,width=50)
            self.tv.column('salario',minwidth=0,width=50)
            self.tv.heading('nome',text="nome")
            self.tv.heading('login',text="login")
            self.tv.heading('senha',text="senha")
            self.tv.heading('email',text="email")
            self.tv.heading('idade',text="idade")
            self.tv.heading('sexo',text="sexo")
            self.tv.heading('cpf',text="cpf")
            self.tv.heading('salario',text="salario")
            self.tv.place(relx=0.005,rely=0.02,relheight=0.80,relwidth=0.99)
            self.lb = Scrollbar(self.tv,orient="vertical",command=self.tv.yview)
            self.lb.pack(side=RIGHT,fill="y")
            self.tv.configure(yscrollcommand=self.lb.set)
            cursor7=conexao.cursor()
            cursor7.execute("SELECT * FROM Info_Funcino")
            resultado=cursor7.fetchall()
            for x in resultado:
                self.tv.insert("","end",values=(tuple(x)))

        def apagar():
            try:
                itemSelecionado=self.tv.selection()[0]
                self.tv.delete(itemSelecionado)
            except:
                messagebox.showinfo(title="ERRO",text="Selecione um elemento a ser deletado")

        def pesquisar_ind():
            pes=slot_pesqui.get()
            cursor33=conexao.cursor()
            cursor33.execute("SELECT nome,login,senha,email,data,sexo,cpf,plano FROM Info_Usua WHERE nome LIKE '%s' ORDER BY nome ASC" % pes)
            resultis=cursor33.fetchall()
            self.lb.destroy()
            self.tv.destroy()
            self.tv=ttk.Treeview(self.frame3,columns=("nome","login","senha","email","idade","sexo","cpf","plano"),show='headings')
            self.tv.column('nome',minwidth=0,width=50)
            self.tv.column('login',minwidth=0,width=50)
            self.tv.column('senha',minwidth=0,width=50)
            self.tv.column('email',minwidth=0,width=50)
            self.tv.column('idade',minwidth=0,width=50)
            self.tv.column('sexo',minwidth=0,width=50)
            self.tv.column('cpf',minwidth=0,width=50)
            self.tv.column('plano',minwidth=0,width=50)
            self.tv.heading('nome',text="nome")
            self.tv.heading('login',text="login")
            self.tv.heading('senha',text="senha")
            self.tv.heading('email',text="email")
            self.tv.heading('idade',text="idade")
            self.tv.heading('sexo',text="sexo")
            self.tv.heading('cpf',text="cpf")
            self.tv.heading('plano',text="plano")
            self.tv.place(relx=0.005,rely=0.02,relheight=0.80,relwidth=0.99)
            self.lb = Scrollbar(self.tv,orient="vertical",command=self.tv.yview)
            self.lb.pack(side=RIGHT,fill="y")
            self.tv.configure(yscrollcommand=self.lb.set)
            for x in resultis:
                self.tv.insert("","end",values=(tuple(x)))
            slot_pesqui.delete(0,END)

        def pesquisar_ind2():
            pes=slot_pesqui.get()
            cursor33=conexao.cursor()
            cursor33.execute("SELECT nome,login,senha,email,data,sexo,cpf,salario FROM Info_Funcino WHERE nome LIKE '%s' ORDER BY nome ASC" % pes)
            resultis=cursor33.fetchall()
            self.lb.destroy()
            self.tv.destroy()
            self.tv=ttk.Treeview(self.frame3,columns=("nome","login","senha","email","idade","sexo","cpf","salario"),show='headings')
            self.tv.column('nome',minwidth=0,width=50)
            self.tv.column('login',minwidth=0,width=50)
            self.tv.column('senha',minwidth=0,width=50)
            self.tv.column('email',minwidth=0,width=50)
            self.tv.column('idade',minwidth=0,width=50)
            self.tv.column('sexo',minwidth=0,width=50)
            self.tv.column('cpf',minwidth=0,width=50)
            self.tv.column('salario',minwidth=0,width=50)
            self.tv.heading('nome',text="nome")
            self.tv.heading('login',text="login")
            self.tv.heading('senha',text="senha")
            self.tv.heading('email',text="email")
            self.tv.heading('idade',text="idade")
            self.tv.heading('sexo',text="sexo")
            self.tv.heading('cpf',text="cpf")
            self.tv.heading('salario',text="salario")
            self.tv.place(relx=0.005,rely=0.02,relheight=0.80,relwidth=0.99)
            self.lb = Scrollbar(self.tv,orient="vertical",command=self.tv.yview)
            self.lb.pack(side=RIGHT,fill="y")
            self.tv.configure(yscrollcommand=self.lb.set)
            for x in resultis:
                self.tv.insert("","end",values=(tuple(x)))
            slot_pesqui.delete(0,END)

        def limp_tela():
            self.lb.destroy()
            self.tv.destroy()
            self.tv=ttk.Treeview(self.frame3,columns=("nome","login","senha","email","idade","sexo","cpf","plano"),show='headings')
            self.tv.column('nome',minwidth=0,width=50)
            self.tv.column('login',minwidth=0,width=50)
            self.tv.column('senha',minwidth=0,width=50)
            self.tv.column('email',minwidth=0,width=50)
            self.tv.column('idade',minwidth=0,width=50)
            self.tv.column('sexo',minwidth=0,width=50)
            self.tv.column('cpf',minwidth=0,width=50)
            self.tv.column('plano',minwidth=0,width=50)
            self.tv.heading('nome',text="nome")
            self.tv.heading('login',text="login")
            self.tv.heading('senha',text="senha")
            self.tv.heading('email',text="email")
            self.tv.heading('idade',text="idade")
            self.tv.heading('sexo',text="sexo")
            self.tv.heading('cpf',text="cpf")
            self.tv.heading('plano',text="plano")
            self.tv.place(relx=0.005,rely=0.02,relheight=0.80,relwidth=0.99)
            self.lb = Scrollbar(self.tv,orient="vertical",command=self.tv.yview)
            self.lb.pack(side=RIGHT,fill="y")
            self.tv.configure(yscrollcommand=self.lb.set)

        def pegar():
            #verificar se preencheu tudo
            if slot_reg_name.get() != '' and slot_reg_log.get() != '' and slot_reg_sen.get()!= '' and slot_reg_email.get() != '' and slot_reg_data.get() != '' and slot_reg_sexo.get() != '' and slot_reg_cpf.get() != '' and slot_reg_plan.get() != '':
                h =slot_reg_cpf.get().replace('.','').replace('-','')
                h_soma_dig1=h_soma_dig2=h_som2=h_verif=h_verif2=0
                contador=10
                contador2=11
                #tratar erros
                try:
                    int(h)
                except ValueError:
                    cpf_error=Label(self.frame1,text="não sabia que cpf agora tinha letras em sua composição",bg="red")
                    cpf_error.place(relx=0.054, rely=0.356, relheight=0.05, relwidth=0.55)
                    cpf_error.after(2500,cpf_error.destroy)

                if len(h)!=11:
                    cpf_error=Label(self.frame1,text="um cpf possui 11 digitos númericos, sem contar com . e - ",bg="red")
                    cpf_error.place(relx=0.054, rely=0.206, relheight=0.05, relwidth=0.55)
                    cpf_error.after(2500,cpf_error.destroy)
                else:
                    #calulo de verificação
                    for c in range (0,9,1):
                        h_soma_dig1+=(int(h[c])*contador)
                        h_soma_dig2+=(int(h[c])*contador2)
                        contador2-=1
                        contador-=1
                    h_soma_dig2+=int(h[9])*2
                    h_som2=(int(h[9])+int(h[10]))
                    h_div=(h_soma_dig1*10)%11
                    h_div2=(h_soma_dig2*10)%11
                    h_verif+=int(h[9])
                    h_verif2+=int(h[10])
                    if h_div == 10:
                        h_div=0
                    if h_div==h_verif and h_div2==h_verif2:
                        valid_cpf=15
                    else:
                        cpf_error=Label(self.frame1,text="cpf invalido!",bg="red")
                        cpf_error.place(relx=0.254, rely=0.306, relheight=0.05, relwidth=0.20)
                        cpf_error.after(2500,cpf_error.destroy)
                #validação data
                idade= slot_reg_data.get()
                try:
                    int(idade) 
                except ValueError:
                    data_error=Label(self.frame1,text="não sabia que idades agora tinham letras em sua composição",bg="red")
                    data_error.place(relx=0.054, rely=0.356, relheight=0.05, relwidth=0.55)
                    data_error.after(2500,data_error.destroy)
                else:
                    if int(idade)<100 and int(idade)>0 :
                            data_valid = 125
                    else:
                        if int(idade)>=100:
                            data_error=Label(self.frame1,text="não aceitamos velhotes de 100 ou mais",bg="red")
                            data_error.place(relx=0.054, rely=0.356, relheight=0.15, relwidth=0.55)
                            data_error.after(2500,data_error.destroy)
                        if int(idade)<=0:
                            data_error=Label(self.frame1,text="é um deus supremo, veio à min antes mesmo\n de nascer",bg="red")
                            data_error.place(relx=0.054, rely=0.356, relheight=0.15, relwidth=0.55)
                            data_error.after(2500,data_error.destroy)
                
                #validação e-mail
                if not'@' in slot_reg_email.get():
                    email_error=Label(self.frame1,text="Isso não é um e-mail, um e-mail tem um @",bg="Red")
                    email_error.place(relx=0.054, rely=0.806, relheight=0.05, relwidth=0.40)
                    email_error.after(2500,email_error.destroy)
                else:
                    try:
                        slot_reg_email.get().index('.')
            
                    except ValueError:
                        email_error=Label(self.frame1,text="um e-mail,é composto por um .com e um exemple antes dele exemplo: nome@example.com",bg="Red")
                        email_error.place(relx=0.054, rely=0.956, relheight=0.05, relwidth=1)
                        email_error.after(2500,email_error.destroy)
                    va=slot_reg_email.get().find('@')
                    vb=slot_reg_email.get().index('.')
                    if vb != va+1:
                        if not ".com" in slot_reg_email.get():
                            email_error=Label(self.frame1,text="um e-mail,é composto por um .com e um exemple antes dele exemplo: nome@example.com",bg="Red")
                            email_error.place(relx=0.054, rely=0.956, relheight=0.05, relwidth=1)
                            email_error.after(2500,email_error.destroy)
                        else:
                            valid_email=32
                    else:
                        email_error=Label(self.frame1,text="um e-mail,é composto por um . mas ele não é ai e um exemple antes dele\nexemplo: nome@example.com",bg="Red")
                        email_error.place(relx=0.304, rely=0.886, relheight=0.12, relwidth=0.75)
                        email_error.after(2500,email_error.destroy)
                if valid_cpf==15 and valid_email==32 and data_valid == 125:
                    reg_nome = slot_reg_name.get()
                    reg_login = slot_reg_log.get()
                    reg_senha = slot_reg_sen.get()
                    reg_email = slot_reg_email.get()
                    reg_data = slot_reg_data.get()
                    reg_sexo = slot_reg_sexo.get()
                    reg_cpf = slot_reg_cpf.get()
                    reg_plan = slot_reg_plan.get()
                    # comando
                    comando = f"""INSERT INTO Info_Usua (nome,cpf,login,senha,email,plano,sexo,data)
                    VALUES 
                        ('{reg_nome}','{reg_cpf}','{reg_login}','{reg_senha}','{reg_email}','{reg_plan}','{reg_sexo}','{reg_data}')"""
                    cursor.execute(comando)
                    cursor.commit()
                    
                    # apagar
                    slot_reg_name.delete(0, END)
                    slot_reg_log.delete(0, END)
                    slot_reg_sen.delete(0, END)
                    slot_reg_email.delete(0, END)
                    slot_reg_data.delete(0, END)
                    slot_reg_sexo.delete(0, END)
                    slot_reg_cpf.delete(0, END)
                    slot_reg_plan.delete(0, END)
                else:
                    cpf_error=Label(self.jan,text="alguma informação está errada!",bg="red")
                    cpf_error.place(relx=0.8,rely=0.15)
                    cpf_error.after(2500,cpf_error.destroy)
            else:
                campos_erro_txt=Label(self.jan,text="Preencha\n todos\n os\n campos!",height=10,width=20,bg="red")
                campos_erro_txt.place(relx=0.40,rely=0.40)
                campos_erro_txt.after(1500,campos_erro_txt.destroy)
        

        ######################## escravos
        def pegar2():
            #verificar se preencheu tudo
            if slot_reg_name2.get() != '' and slot_reg_log2.get() != '' and slot_reg_sen2.get()!= '' and slot_reg_email2.get() != '' and slot_reg_data2.get() != '' and slot_reg_sexo2.get() != '' and slot_reg_cpf2.get() != '' and slot_reg_plan2.get() != '':
                h =slot_reg_cpf2.get().replace('.','').replace('-','')
                h_soma_dig1=h_soma_dig2=h_som2=h_verif=h_verif2=0
                contador=10
                contador2=11
                #tratar erros
                try:
                    int(h)
                except ValueError:
                    cpf_error=Label(self.frame2,text="não sabia que cpf agora tinha letras em sua composição",bg="red")
                    cpf_error.place(relx=0.054, rely=0.356, relheight=0.05, relwidth=0.55)
                    cpf_error.after(2500,cpf_error.destroy)

                if len(h)!=11:
                    cpf_error=Label(self.frame2,text="um cpf possui 11 digitos númericos, sem contar com . e - ",bg="red")
                    cpf_error.place(relx=0.054, rely=0.206, relheight=0.05, relwidth=0.55)
                    cpf_error.after(2500,cpf_error.destroy)
                else:
                    #calulo de verificação
                    for c in range (0,9,1):
                        h_soma_dig1+=(int(h[c])*contador)
                        h_soma_dig2+=(int(h[c])*contador2)
                        contador2-=1
                        contador-=1
                    h_soma_dig2+=int(h[9])*2
                    h_som2=(int(h[9])+int(h[10]))
                    h_div=(h_soma_dig1*10)%11
                    h_div2=(h_soma_dig2*10)%11
                    h_verif+=int(h[9])
                    h_verif2+=int(h[10])
                    if h_div == 10:
                        h_div=0
                    if h_div==h_verif and h_div2==h_verif2:
                        valid_cpf=15
                    else:
                        cpf_error=Label(self.frame2,text="cpf invalido!",bg="red")
                        cpf_error.place(relx=0.254, rely=0.306, relheight=0.05, relwidth=0.20)
                        cpf_error.after(2500,cpf_error.destroy)
                #validação data
                idade= slot_reg_data2.get()
                try:
                    int(idade) 
                except ValueError:
                    data_error=Label(self.frame1,text="não sabia que idades agora tinham letras em sua composição",bg="red")
                    data_error.place(relx=0.054, rely=0.356, relheight=0.05, relwidth=0.55)
                    data_error.after(2500,data_error.destroy)
                else:
                    if int(idade)<100 and int(idade)>0 :
                            data_valid = 125
                    else:
                        if int(idade)>=100:
                            data_error=Label(self.frame1,text="não aceitamos velhotes de 100 ou mais",bg="red")
                            data_error.place(relx=0.054, rely=0.356, relheight=0.15, relwidth=0.55)
                            data_error.after(2500,data_error.destroy)
                        if int(idade)<=0:
                            data_error=Label(self.frame1,text="é um deus supremo, veio à min antes mesmo\n de nascer",bg="red")
                            data_error.place(relx=0.054, rely=0.356, relheight=0.15, relwidth=0.55)
                            data_error.after(2500,data_error.destroy)
                
                #validação e-mail
                if not'@' in slot_reg_email2.get():
                    email_error=Label(self.frame2,text="Isso não é um e-mail, um e-mail tem um @",bg="Red")
                    email_error.place(relx=0.054, rely=0.806, relheight=0.05, relwidth=0.40)
                    email_error.after(2500,email_error.destroy)
                else:
                    try:
                        slot_reg_email2.get().index('.')
            
                    except ValueError:
                        email_error=Label(self.frame2,text="um e-mail,é composto por um .com e um exemple antes dele exemplo: nome@example.com",bg="Red")
                        email_error.place(relx=0.054, rely=0.956, relheight=0.05, relwidth=1)
                        email_error.after(2500,email_error.destroy)
                    va=slot_reg_email2.get().find('@')
                    vb=slot_reg_email2.get().index('.')
                    if vb != va+1:
                        if not ".com" in slot_reg_email2.get():
                            email_error=Label(self.frame2,text="um e-mail,é composto por um .com e um exemple antes dele exemplo: nome@example.com",bg="Red")
                            email_error.place(relx=0.054, rely=0.956, relheight=0.05, relwidth=1)
                            email_error.after(2500,email_error.destroy)
                        else:
                            valid_email=32
                    else:
                        email_error=Label(self.frame2,text="um e-mail,é composto por um . mas ele não é ai e um exemple antes dele\nexemplo: nome@example.com",bg="Red")
                        email_error.place(relx=0.304, rely=0.886, relheight=0.12, relwidth=0.75)
                        email_error.after(2500,email_error.destroy)
                if valid_cpf==15 and valid_email==32 and data_valid==125:
                    reg_nome = slot_reg_name2.get()
                    reg_login = slot_reg_log2.get()
                    reg_senha = slot_reg_sen2.get()
                    reg_email = slot_reg_email2.get()
                    reg_data = slot_reg_data2.get()
                    reg_sexo = slot_reg_sexo2.get()
                    reg_cpf = slot_reg_cpf2.get()
                    reg_plan = slot_reg_plan2.get()
                    # comando
                    comando = f"""INSERT INTO Info_Funcino (nome,cpf,login,senha,email,salario,sexo,data)
                    VALUES 
                        ('{reg_nome}','{reg_cpf}','{reg_login}','{reg_senha}','{reg_email}','{reg_plan}','{reg_sexo}','{reg_data}')"""
                    cursor.execute(comando)
                    cursor.commit()
                    # apagar
                    slot_reg_name2.delete(0, END)
                    slot_reg_log2.delete(0, END)
                    slot_reg_sen2.delete(0, END)
                    slot_reg_email2.delete(0, END)
                    slot_reg_data2.delete(0, END)
                    slot_reg_sexo2.delete(0, END)
                    slot_reg_cpf2.delete(0, END)
                    slot_reg_plan2.delete(0, END)
                else:
                    cpf_error=Label(self.jan,text="alguma informação está errada!",bg="red")
                    cpf_error.place(relx=0.8,rely=0.15)
                    cpf_error.after(2500,cpf_error.destroy)
            else:
                campos_erro_txt=Label(self.jan,text="Preencha\n todos\n os\n campos!",height=10,width=20,bg="red")
                campos_erro_txt.place(relx=0.40,rely=0.40)
                campos_erro_txt.after(1500,campos_erro_txt.destroy)


        def play2_para():
            global contador
            if contador%2==0:
                pygame.mixer.music.stop()
                contador+=1
            else:
                pygame.mixer.music.load("pngs\Mag_Quer_Tomar_Bomba.mp3")
                pygame.mixer.music.play(loops=999999)
                contador+=1
        #som botão
        imgbb=PhotoImage(file="pngs\labobora.png").subsample(5,5)
        but_music = Button(self.jan,image=imgbb,command=play2_para)
        but_music.place(relx=0.00, rely=0.00, relheight=0.06, relwidth=0.06)

        #mais botão
        but_music_volu = Button(self.jan,text="+",command=Func.vol_som)
        but_music_volu.place(relx=0.09, rely=0.00, relheight=0.03, relwidth=0.03)
        
        #menos botão
        but_music_volu2 = Button(self.jan,text="-",command=Func.vol_sub)
        but_music_volu2.place(relx=0.12, rely=0.00, relheight=0.03, relwidth=0.03)
        noot=ttk.Notebook(self.jan)
        noot.place(relx=0.02,rely=0.4,relwidth=0.96,relheight=0.575)

        self.frame1=Frame(noot,bg="#A9A9A9")
        noot.add(self.frame1,text="Registrar")

        self.frame2=Frame(noot,bg="#A9A9A9")
        noot.add(self.frame2,text="Registro Funcionários")

        self.frame3=Frame(noot,bg="#A9A9A9")
        noot.add(self.frame3,text="Banco de dados")

        self.tv=ttk.Treeview(self.frame3,columns=("nome","login","senha","email","idade","sexo","cpf","plano"),show='headings')
        self.tv.column('nome',minwidth=0,width=50)
        self.tv.column('login',minwidth=0,width=50)
        self.tv.column('senha',minwidth=0,width=50)
        self.tv.column('email',minwidth=0,width=50)
        self.tv.column('idade',minwidth=0,width=50)
        self.tv.column('sexo',minwidth=0,width=50)
        self.tv.column('cpf',minwidth=0,width=50)
        self.tv.column('plano',minwidth=0,width=50)
        self.tv.heading('nome',text="nome")
        self.tv.heading('login',text="login")
        self.tv.heading('senha',text="senha")
        self.tv.heading('email',text="email")
        self.tv.heading('idade',text="idade")
        self.tv.heading('sexo',text="sexo")
        self.tv.heading('cpf',text="cpf")
        self.tv.heading('plano',text="plano")
        self.tv.place(relx=0.005,rely=0.02,relheight=0.80,relwidth=0.98)
        self.lb = Scrollbar(self.tv,orient="vertical",command=self.tv.yview)
        self.lb.pack(side=RIGHT,fill="y")
        self.tv.configure(yscrollcommand=self.lb.set)

        botuu_11=Button(self.jan,text="chat",command=chat34)
        botuu_11.place(relx=0.00,rely=0.28,relheight=0.10,relwidth=0.17)
        botuu_1=Button(self.frame3,text="Mostra funcionarios",command=inserir2)
        botuu_1.place(relx=0.00,rely=0.90,relheight=0.10,relwidth=0.17)
        botuu=Button(self.frame3,text="Mostra usuarios",command=inserir)
        botuu.place(relx=0.17,rely=0.90,relheight=0.10,relwidth=0.17)
        slot_pesqui=Entry(self.frame3)
        slot_pesqui.place(relx=0.41,rely=0.83,relheight=0.05,relwidth=0.20)
        botuu1=Button(self.frame3,text="buscar usuario",command=pesquisar_ind)
        botuu1.place(relx=0.51,rely=0.90,relheight=0.10,relwidth=0.17)
        botuu2=Button(self.frame3,text="apagar",command=apagar)
        botuu2.place(relx=0.68,rely=0.90,relheight=0.10,relwidth=0.17)
        botuu3=Button(self.frame3,text="limpar",command=limp_tela)
        botuu3.place(relx=0.85,rely=0.90,relheight=0.10,relwidth=0.17)
        botuu4=Button(self.frame3,text="buscar funcionario",command=pesquisar_ind2)
        botuu4.place(relx=0.34,rely=0.90,relheight=0.10,relwidth=0.17)



        sexo_list = ["Masculino", "Feminino", "Trans", "Binario", "Helicoptero de Combate",
                    "Geladeira Eletrolux Três Portas", "Megazord", "Outro"]
        plano_list =["Básico – R$ 70.00", "Médio - R$ 90.00", "Completo – R$ 120.00"]
        plano_list_func =["Professor -salário: 0,14¢ à hora","gerente -salário: 0,37¢ à hora", "faxineiro -salário: 0,05¢ à hora"]

#################CADASTRO ALUNIOS
                ######################### slots
        slot_reg_name = Entry(self.frame1)  # nome
        slot_reg_name.place(relx=0.054, rely=0.106, relheight=0.05, relwidth=0.37)

        slot_reg_cpf = Entry(self.frame1)  # cpf
        slot_reg_cpf.place(relx=0.054, rely=0.306, relheight=0.05, relwidth=0.37)

        slot_reg_log = Entry(self.frame1)  # login
        slot_reg_log.place(relx=0.054, rely=0.506, relheight=0.05, relwidth=0.37)

        slot_reg_plan = ttk.Combobox(self.frame1,values=plano_list,state="readonly")  # plano
        slot_reg_plan.place(relx=0.554, rely=0.106, relheight=0.05, relwidth=0.37)

        slot_reg_sen = Entry(self.frame1, show="*")  # senha
        slot_reg_sen.place(relx=0.054, rely=0.706, relheight=0.05, relwidth=0.37)

        slot_reg_email = Entry(self.frame1)  # e-mail
        slot_reg_email.place(relx=0.054, rely=0.906, relheight=0.05, relwidth=0.37)

        slot_reg_data = Entry(self.frame1)  # data de nascimento
        slot_reg_data.place(relx=0.554, rely=0.506, relheight=0.05, relwidth=0.37)

        slot_reg_sexo = ttk.Combobox(self.frame1, values=sexo_list)  # sexo
        slot_reg_sexo.place(relx=0.554, rely=0.306, relheight=0.05, relwidth=0.37)

        # textos
        slot_reg_name_txt = Label(self.frame1, text="Nome Completo",bg="#00FA9A")  # nome
        slot_reg_name_txt.place(relx=0.054, rely=0.056, relheight=0.05, relwidth=0.37)
    
        slot_reg_cpf_txt = Label(self.frame1, text="Cpf",bg="#00FA9A")  # cpf
        slot_reg_cpf_txt.place(relx=0.054, rely=0.256, relheight=0.05, relwidth=0.37)

        slot_reg_log_txt = Label(self.frame1, text="Criar Login")  # login
        slot_reg_log_txt.place(relx=0.054, rely=0.456, relheight=0.05, relwidth=0.37)
        slot_reg_log_txt.config(bg="#00FA9A")

        slot_reg_plan_txt = Label(self.frame1, text="Selecione um plano")  # plano
        slot_reg_plan_txt.place(relx=0.554, rely=0.056, relheight=0.05, relwidth=0.37)
        slot_reg_plan_txt.config(bg="#00FA9A")

        slot_reg_sen_txt = Label(self.frame1, text="Criar Senha")  # senha
        slot_reg_sen_txt.place(relx=0.054, rely=0.656, relheight=0.05, relwidth=0.37)
        slot_reg_sen_txt.config(bg="#00FA9A")

        slot_reg_email_txt = Label(self.frame1, text="E-mail")  # e-mail
        slot_reg_email_txt.place(relx=0.054, rely=0.856, relheight=0.05, relwidth=0.37)
        slot_reg_email_txt.config(bg="#00FA9A")

        slot_reg_data_txt = Label(self.frame1, text="idade")  # data de nascimento
        slot_reg_data_txt.place(relx=0.554, rely=0.456, relheight=0.05, relwidth=0.37)
        slot_reg_data_txt.config(bg="#00FA9A")

        slot_reg_sexo_txt = Label(self.frame1, text="Sexo")  # sexo
        slot_reg_sexo_txt.place(relx=0.554, rely=0.256, relheight=0.05, relwidth=0.37)
        slot_reg_sexo_txt.config(bg="#00FA9A")

        # botão
        but_cad = Button(self.frame1, text="Cadastrar", command=pegar, font=("", 12), bg="#98FB98")
        but_cad.place(relx=0.554, rely=0.606, relheight=0.05, relwidth=0.16)

########### CADASTRO ESCRAVOS (funcionarios)
        ######################### slots
        slot_reg_name2 = Entry(self.frame2)  # nome
        slot_reg_name2.place(relx=0.054, rely=0.106, relheight=0.05, relwidth=0.37)

        slot_reg_cpf2 = Entry(self.frame2)  # cpf
        slot_reg_cpf2.place(relx=0.054, rely=0.306, relheight=0.05, relwidth=0.37)

        slot_reg_log2 = Entry(self.frame2)  # login
        slot_reg_log2.place(relx=0.054, rely=0.506, relheight=0.05, relwidth=0.37)

        slot_reg_plan2 = ttk.Combobox(self.frame2,values=plano_list_func,state="readonly")  # plano
        slot_reg_plan2.place(relx=0.554, rely=0.106, relheight=0.05, relwidth=0.37)

        slot_reg_sen2 = Entry(self.frame2, show="*")  # senha
        slot_reg_sen2.place(relx=0.054, rely=0.706, relheight=0.05, relwidth=0.37)

        slot_reg_email2 = Entry(self.frame2)  # e-mail
        slot_reg_email2.place(relx=0.054, rely=0.906, relheight=0.05, relwidth=0.37)

        slot_reg_data2 = Entry(self.frame2)  # data de nascimento
        slot_reg_data2.place(relx=0.554, rely=0.506, relheight=0.05, relwidth=0.37)

        slot_reg_sexo2 = ttk.Combobox(self.frame2, values=sexo_list)  # sexo
        slot_reg_sexo2.place(relx=0.554, rely=0.306, relheight=0.05, relwidth=0.37)

        # textos
        slot_reg_name_txt = Label(self.frame2, text="Nome Completo",bg="#00FA9A")  # nome
        slot_reg_name_txt.place(relx=0.054, rely=0.056, relheight=0.05, relwidth=0.37)
    
        slot_reg_cpf_txt = Label(self.frame2, text="Cpf",bg="#00FA9A")  # cpf
        slot_reg_cpf_txt.place(relx=0.054, rely=0.256, relheight=0.05, relwidth=0.37)

        slot_reg_log_txt = Label(self.frame2, text="Criar Login")  # login
        slot_reg_log_txt.place(relx=0.054, rely=0.456, relheight=0.05, relwidth=0.37)
        slot_reg_log_txt.config(bg="#00FA9A")

        slot_reg_plan_txt = Label(self.frame2, text="Selecione um Cargo")  # plano
        slot_reg_plan_txt.place(relx=0.554, rely=0.056, relheight=0.05, relwidth=0.37)
        slot_reg_plan_txt.config(bg="#00FA9A")

        slot_reg_sen_txt = Label(self.frame2, text="Criar Senha")  # senha
        slot_reg_sen_txt.place(relx=0.054, rely=0.656, relheight=0.05, relwidth=0.37)
        slot_reg_sen_txt.config(bg="#00FA9A")

        slot_reg_email_txt = Label(self.frame2, text="E-mail")  # e-mail
        slot_reg_email_txt.place(relx=0.054, rely=0.856, relheight=0.05, relwidth=0.37)
        slot_reg_email_txt.config(bg="#00FA9A")

        slot_reg_data_txt = Label(self.frame2, text="idade")  # data de nascimento
        slot_reg_data_txt.place(relx=0.554, rely=0.456, relheight=0.05, relwidth=0.37)
        slot_reg_data_txt.config(bg="#00FA9A")

        slot_reg_sexo_txt = Label(self.frame2, text="Sexo")  # sexo
        slot_reg_sexo_txt.place(relx=0.554, rely=0.256, relheight=0.05, relwidth=0.37)
        slot_reg_sexo_txt.config(bg="#00FA9A")

        # botão
        but_cad2 = Button(self.frame2, text="Cadastrar", command=pegar2, font=("", 12), bg="#98FB98")
        but_cad2.place(relx=0.554, rely=0.606, relheight=0.05, relwidth=0.16)


########## THE END ####################
        self.jan.mainloop()
########## R.I.P####################

#INVOCAÇÃO / O RENASCIMENTO
#|||||||||
#VVVVVVVVV
Tela_Login()