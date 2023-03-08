# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:42:55 2023

@author: alexa
"""
import tkinter as ttk
from tkinter import *
import openai
openai.api_key='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'

from tkinter import messagebox

Ventana = Tk()

def exit_application():
    msg_box = messagebox.askquestion('Ne parasesti?', 'Doresti sa iesi din aplicatie?',
                                        icon='warning')
    if msg_box == 'yes':
        Ventana.destroy()
    else:
        ttk.messagebox.showinfo('Ce bine!!!', 'Te vei intoarce la aplicatie.')


def Copiar(*args):
   
    y=Captura.get()
    if y=='exit':
        Ventana.destroy()
    else:
        
        completion = openai.Completion.create(model= "text-davinci-003",
                                              prompt = y ,
                                                # temperature=0,
                                              max_tokens = 2048)
        
        bak= completion.choices[0].text
        text=(bak)
        textcomp.replace(1.0, END, text)
 
 #Creamos raíz

Ventana.resizable(False,False) #Impedimos redimensionar la ventana
Ventana.geometry("650x400") #Tamaño por defecto
Ventana.title("Python: ChatGPT") #Titulo de ventana
questionframe=ttk.Frame(Ventana)
questionframe.grid(column=0, row=1,sticky=W, padx=5)
ttk.Label(questionframe, text="Intrebare:").grid(column=0, row=1, sticky=W)
#Variable de captura de texto
Captura = StringVar()
#Variable de resultado
Resultado = StringVar()
#Cremos campo de texto
Entrada = Entry(questionframe, width=85)
Entrada.grid(row=2, column=0,sticky=W,padx=5)
Entrada.config(textvariable=Captura) #El texto se guarda en Captura

#Creamos botón
Boton = Button(questionframe, text="Intreaba:", command = Copiar, bg='blue', fg='white') #Llama a Copiar
Boton.grid(row=2, column=1,sticky=W,padx=5)

Boton_Exit = Button(questionframe, text=" Iesire ", command = exit_application, bg='brown', fg='white') #Llama a Copiar
Boton_Exit.grid(row=2, column=2,sticky=W,padx=3)


frame=ttk.Frame(Ventana)
frame.grid(column=0, row=3,sticky=W, padx=5)
ttk.Label(frame, text="Raspuns:").grid(column=1, row=3, sticky=W)
#Cremos label 
Etiqueta=ttk.Frame(Ventana)
Etiqueta.grid(row=4, column=0, sticky=W, padx=5)
textcomp=Text(Etiqueta, width=77, height=20)
textcomp.grid(column=1, row=4, sticky=W)

Entrada.focus()
Ventana.bind('<Return>', Copiar)

scrollbar= Scrollbar(Etiqueta, command=textcomp.yview)
scrollbar.grid(column=2, row=4, sticky=(W,N,S))
textcomp['yscrollcommand']=scrollbar.set


#Bucle de aplicación
Ventana.mainloop()
