from tkinter import *
import pyperclip

def cri():
    chave=int(chave_e.get())
    #chave_e.delete(0,END)
    palavra=entrada.get("1.0",END)
    entrada.delete("1.0",END)
    palavrac=""
    for letras in palavra:
        v=ord(letras)
        if chave>=0 and chave<=100000:
            v+=chave
        else:
            v=""
            label2=Label(jan,bg="Red",foreground="yellow",text="apenas números de \n 0 a 100.000 vc nem vai usar td isso cara !")
            label2.place(relx=0.27,rely=0.10,relheight=0.35,relwidth=0.55)
            label2.after(2500, label2.destroy)

        nv=chr(v)
        palavrac+=nv
   
    pyperclip.copy(palavrac)
    label=Label(jan,bg="blue",foreground="yellow",text=palavrac+" \n"+"copiado para o crtl")
    label.place(relx=0.27,rely=0.10,relheight=0.35,relwidth=0.55)
    label.after(2500, label.destroy)
def dcri():
    chave=int(chave_e.get())
    #chave_e.delete(0,END)
    palavra=entrada.get("1.0",END)
    entrada.delete("1.0",END)
    palavrac=""
    for letras in palavra:
        v2=ord(letras)
        if chave>=0 and chave<=100000:
            v2+=(chave*-1)
            if v2>0:
                pass
            else:
                v2=0
        else:
            v2=""
            label2=Label(jan,bg="Red",foreground="yellow",text="apenas números de \n 0 a 10000 vc nem vai usar td isso cara !")
            label2.place(relx=0.27,rely=0.10,relheight=0.35,relwidth=0.55)
            label2.after(2500, label2.destroy)

        nv=chr(v2)

        palavrac+=nv

    pyperclip.copy(palavrac)
    label=Label(jan,bg="blue",foreground="yellow",text=palavrac+" \n"+"copiado para o crtl")
    label.place(relx=0.27,rely=0.10,relheight=0.35,relwidth=0.55)
    label.after(2500, label.destroy)

jan=Tk()

jan.config(background="#9932CC",cursor="spider")
jan.title("Pandora")

entrada=Text(jan,bg="purple",foreground="#FFFF00",insertbackground="yellow",cursor="target")
entrada.place(relx=0, rely=0.50, relheight=0.3, relwidth=0.5)
info=Label(text="Anotações",background="black",foreground="yellow")
info.place(relx=0.7, rely=0.40, relheight=0.10, relwidth=0.275)
anota=Text(jan,bg="black",foreground="white",insertbackground="yellow",cursor="target")
anota.place(relx=0.5, rely=0.50, relheight=0.3, relwidth=0.5)
chave_e=Entry(jan,bg="purple",foreground="#FFDAB9",font=15,insertbackground="yellow",cursor="target")
chave_e.place(relx=0.45,rely=0.20,relheight=0.10,relwidth=0.10)
cri_buton=Button(text="cripto",bg="#00FA9A",command=cri,cursor="dotbox")
cri_buton.place(relx=0, rely=0.80,relheight=0.08,relwidth=0.20)
dcri_buton=Button(text="descript",bg="#20B2AA",command=dcri,cursor="dotbox")
dcri_buton.place(relx=0.75, rely=0.80,relheight=0.08,relwidth=0.25)



jan.mainloop()

#alfabeto= abcdefghijklmnopqrstuvwxyz
#numeros= 0123456789
#ascentos= ´[~],.;`{^}<>:
#char especial = ç áéíóú âêîôû ãõ /*-+=

