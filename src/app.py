import tkinter
from tkinter import *

janela = Tk('Sistema de Gerenciamento de Usuário')
janela.geometry('400x300')

titulo = Label(janela, text='CRUD', font=('Arial',20))
titulo.pack(pady=30)

nome = Label(janela, text='Nome:')
nome.place(x=50,y=100)

email = Label(janela, text='Email:')
email.place(x=50,y=130)

senha = Label(janela, text='Senha:')
senha.place(x=50,y=160)

enviar = Button(janela, text='Cadastrar', width=10)
enviar.place(x=100,y=200)

listar = Button(janela, text='Listar Usuários', width=15)
listar.place(x=200,y=200)

janela.mainloop()

