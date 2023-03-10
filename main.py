from tkinter import *

import os

# Root config
root = Tk()
sizeRoot = root.geometry("1330x760+100+0")
root.title("Login App")
root.columnconfigure(3, weight=6)
root.rowconfigure(5, weight=3)


#Image background
img = PhotoImage(file="assets/banner_retro.png")
labelImg = Label(root, image=img).place(x=0, y=0)

# Root title
titleLabel = Label(root, 
text="CREAR CUENTA DE USUARIO", 
bg="black", 
fg="white", 
padx=10, 
pady=10,
font=("MV Boli", 20))
titleLabel.grid(columnspan=5, sticky=N+E+S+W)

#Icono App
icono = PhotoImage(file="assets/icon_gui.png")
root.iconphoto(True, icono)


#Campo usuario
userLabel = Label(root, text="Nombre de usuario", width=20, font=("MV Boli", 16), bg="silver").grid(row=2, column=0, pady=20, padx=50)
username_entry = Entry(root, width=40, font=("MV Boli", 16), bg="silver")
username_entry.insert(0, "")
username_entry.grid(row=2, column=1)


#Campo password
passwordLabel = Label(root, text="Contraseña", width=20, font=("MV Boli", 16), bg="silver").grid(row=3, column=0, pady=20, padx=50)
password_entry = Entry(root, width=40, show='*', font=("MV Boli", 16), bg="silver")
password_entry.insert(0, '')
password_entry.grid(row=3, column=1, pady=5)

# Componentes
myButton = Button(root, text="LOGIN", width=20, font=("MV Boli", 14), bg="silver", command=lambda: newUser())
myButton.grid(row=2, column=2, padx=40, pady=10)

btn_show_log = Button(root, text= "Usuarios registrados (Excel)", font=("MV Boli", 16), bg="silver", command=lambda: openLog())
btn_show_log.grid(row=3, column=2)

# Crea un nuevo usuario en un archivo Excel
def newUser():
    file = open("Registros/Users.xls", "a")
    file.write(str('Username: ' + username_entry.get() + '\n'))
    file.write(str('Password: ' + password_entry.get() + '\n'))
    file.close()

# Abre el Excel con el registro de usuarios
def openLog():
    os.system("start EXCEL.EXE Registros/Users.xls")
    
root.mainloop()