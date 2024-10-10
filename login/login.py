import tkinter
import customtkinter
from PIL import Image
from customtkinter import *
import base_de_logeo as bd
from tkinter import messagebox
import re 

root_tk = tkinter.Tk()
root_tk.geometry("400x400")
root_tk.title("Login")

c_negro = '#010101'
c_morado = '#7f5af0'
c_verde = '#2cb67d'

patron_mail = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
patron_texto = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$"
patron_numero = r"^[0-9]+(\.[0-9]+)?$"

def esconder():
    root_tk.withdraw()  

def mostrar():
    root_tk.deiconify()  

def regex_text(char):
    if re.match(patron_texto,char):
        return True
    return False

def regex_email(char):
    if re.match(patron_mail,char):
        return True
    return False
def regex_numer(numero):
    if re.match(patron_numero,numero):
        return True
    return False


def inicio_de_sesion():
    user=CTkEntry.get(usuario)
    passw=CTkEntry.get(contraseña)
    inicio=bd.buscar_usuario(user,passw)
    if inicio:
        messagebox.showinfo('inicio','Ingreso confirmado')
    else:
        messagebox.showerror('inicio','Usuario no encontrado')
        
def mensaje_error_credenciales(text):
    messagebox.showerror('Error','Error en el campo'+text)
    
def registrarse():
    esconder()
    def registro():
        user=CTkEntry.get(correo)
        contra=CTkEntry.get(contraseña)
        cell=CTkEntry.get(telefono)
        name=CTkEntry.get(nombre)
        if not regex_email(user):
            mensaje_error_credenciales('Usuario')
        elif not regex_numer(cell):
            mensaje_error_credenciales('Teléfono')       
        else:
            valor = bd.registrar(name, cell, user, contra)
            print(valor)
            if valor is True:
                messagebox.showinfo('Registro', 'Su registro fue exitoso')
                top.destroy()
                mostrar()
                
            else:
                messagebox.showerror('Falló el registro','El correo esta en uso')
        
        
    top = CTkToplevel(frame)
    top.geometry("380x500")
    top.title("Registro")
    my_image = customtkinter.CTkImage(light_image=light_image,
                                   size=(200, 200))
    image_label = customtkinter.CTkLabel(top, image=my_image, text="")
    image_label.place(relx=0.5, rely=0.20, anchor=tkinter.CENTER)
    
    # Campo de entrada para el correo electrónico
    contraseña = customtkinter.CTkEntry(master=top,
                                    width=220,
                                    height=30,
                                    corner_radius=10,
                                    placeholder_text='contraseña')
    contraseña.place(relx=0.5, rely=0.53, anchor=tkinter.CENTER)

    # Campo de entrada para la contraseña
    telefono = customtkinter.CTkEntry(master=top,
                                        width=220,
                                        height=30,
                                        corner_radius=10,
                                        placeholder_text='telefono')
    telefono.place(relx=0.5, rely=0.61, anchor=tkinter.CENTER)
    
    # Campo de entrada para el nombre
    nombre = customtkinter.CTkEntry(master=top,
                                    width=220,
                                    height=30,
                                    corner_radius=10,
                                    placeholder_text='nombre')
    nombre.place(relx=0.5, rely=0.37, anchor=tkinter.CENTER)

    # Campo de entrada para el telefono
    correo = customtkinter.CTkEntry(master=top,
                                        width=220,
                                        height=30,
                                        corner_radius=10,
                                        placeholder_text='correo')
    correo.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
    
    button = customtkinter.CTkButton(master=top,
                                   text="Registrarse",
                                   command=registro,
                                   width=120,
                                   height=32,
                                   border_width=2,
                                   corner_radius=8,
                                   fg_color=("lightgray", "grey"))
    button.place(relx=0.5, rely=0.70, anchor=tkinter.CENTER)
    
    button_menu = customtkinter.CTkButton(master=top,
                                   text="Menu",
                                   width=120,
                                   height=32,
                                   border_width=2,
                                   corner_radius=8,
                                   fg_color=("lightgray", "grey"))
    button_menu.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)
    

frame = customtkinter.CTkFrame(master=root_tk,
                               width=500,
                               height=500,
                               corner_radius=10,
                               fg_color=c_negro)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Carga la imagen
light_image = Image.open(r"C:\Users\naza\Desktop\Cod\login\2-min_preview_rev_1.png")  # Asegúrate de usar r'' para la ruta
my_image = customtkinter.CTkImage(light_image=light_image,
                                   size=(200, 200))

# Crea un CTkLabel para mostrar la imagen dentro del marco
image_label = customtkinter.CTkLabel(frame, image=my_image, text="")
image_label.place(relx=0.5, rely=0.30, anchor=tkinter.CENTER)  # Posiciona la imagen arriba

# Campo de entrada para el correo electrónico
usuario = customtkinter.CTkEntry(master=frame,
                                   width=220,
                                   height=30,
                                   corner_radius=10,
                                   placeholder_text='Correo electrónico')
usuario.place(relx=0.5, rely=0.53, anchor=tkinter.CENTER)

# Campo de entrada para la contraseña
contraseña = customtkinter.CTkEntry(master=frame,
                                     width=220,
                                     height=30,
                                     corner_radius=10,
                                     placeholder_text='Contraseña',
                                    show='*')                              
contraseña.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

# Botón de inicio de sesión
button = customtkinter.CTkButton(master=frame,
                                   text="Logear",
                                   command=inicio_de_sesion,
                                   width=120,
                                   height=32,
                                   border_width=2,
                                   corner_radius=8,
                                   fg_color=("lightgray", "black"))
button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

button_registro = customtkinter.CTkButton(master=frame,
                                   text="registrarse",
                                   command=registrarse,
                                   width=120,
                                   height=32,
                                   border_width=2,
                                   corner_radius=8,
                                   fg_color=("lightgray", "black"))
button_registro.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

root_tk.mainloop()
