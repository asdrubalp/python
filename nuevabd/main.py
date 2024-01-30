from tkinter import *
from tkinter import messagebox
import sqlite3
class usuario:
    def __init__(self):
        root=Tk()
        root.title("Contabilidad de Licdo. Elys Santaella")
        root.geometry("350x350")
        root.resizable(0,0)
        #Declaración d elas variables
        myAccountID=StringVar()
        myLogin=StringVar()
        ###################Procedimientos
        #Salir del programa
        def salirAplicacion():
            valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
            if valor=="yes":
                root.destroy()
        #Resetear los valores de los campos
        def limpiarCampos():
            myAccountID.set("")
            myLogin.set("")
        def mostrarLicencia():
                print("Esto es Software 100% Libre")
        def mostrarAutor():
                print("Copyleft(2021): José Santaella jsantaella70")
        #CRUD: Create(crear un registro e incluirlo)
        def crear():
            miConexion=sqlite3.connect("contable.DB")
            miCursor=miConexion.cursor()
            datos=myAccountID.get(),myLogin.get()
            miCursor.execute("SELECT * FROM accountTB WHERE accountID=" +myAccountID.get())
            exist = miCursor.fetchone()
            print(exist)
            if exist is None:
                print('Nuevo usuario')
                miCursor.execute("INSERT INTO accountID VALUES(?,?)", (datos))
                miConexion.commit()
                messagebox.showinfo("Registro insertado con éxito")
            else:
                print('Usuario ya registrado')
        #CRUD: Read(leer un registro y mostrar los campos consultados)
        def leer():
            if (myAccountID.get()!=""):
                miConexion=sqlite3.connect("contable.DB")
                miCursor=miConexion.cursor()
                miCursor.execute("SELECT * FROM accountTB WHERE accountID = " +myAccountID.get())
                elUsuario=miCursor.fetchall()
                for usuario in elUsuario:
                    myAccountID.set(usuario[0])
                    myLogin.set(usuario[1])
                miConexion.commit()
            else:
                print("campo vacíoooo")
        #CRUD: Update(actualizar un registro al modificar según los valores de los widgets entry)
        def actualizar():
            miConexion=sqlite3.connect("contable.DB")
            miCursor=miConexion.cursor()
            datos=myAccountID.get(), myLogin.get()
            miCursor.execute("UPDATE accountTB SET accountID=?, login=? WHERE accountID="+myAccountID.get(),(datos))
            miConexion.commit()
            messagebox.showinfo("Registro actualizado con éxito")
        #CRUD: Delete(borrar un registro según el ID del entry del Password)
        def borrar():
            miConexion=sqlite3.connect("contable.DB")
            miCursor=miConexion.cursor()
            miCursor.execute("DELETE FROM accountTB WHERE accountID = "+myAccountID.get())
            miConexion.commit()
            messagebox.showinfo("Registro borrado con éxito")
        def listar():
            miConexion=sqlite3.connect("contable.DB")
            miCursor=miConexion.cursor()
            miCursor.execute("SELECT * FROM accountID")
            elUsuario=miCursor.fetchall()
            #imprimir aquie el numero de filas.. print('Número de filas', elUsuario.length())
            registerCounter=1
            for usuario in elUsuario:
                print(registerCounter,usuario[0]," ",usuario[1])
                registerCounter=registerCounter+1
            miConexion.commit()
        #comienzo del programa
        #Widgets para captar datos
        l1=Label(root, text="Passwd: ")
        l1.grid(column=0, row=1)
        e1=Entry(root, textvariable=myAccountID)
        e1.grid(column=1, row=1)
        l2=Label(root, text="Login: ")
        l2.grid(column=0, row=2)
        e2=Entry(root, textvariable=myLogin)
        e2.grid(column=1, row=2)
        #Botones
        b1=Button(root, text="Create", command=crear)
        b1.place(x=40,y=250)
        b2=Button(root, text="Read", command=leer)
        b2.place(x=90,y=250)
        b3=Button(root, text="Update", command=actualizar)
        b3.place(x=130,y=250)
        b4=Button(root, text="Delete", command=borrar)
        b4.place(x=180,y=250)
        b5=Button(root, text="Limpiar", command=limpiarCampos)
        b5.place(x=40,y=300)
        b6=Button(root, text="Listar", command=listar)
        b6.place(x=90,y=300)
        #metodo del ciclo de la ventana principal
        root.mainloop()
#se crea un objeto appOperador de clase Usuario
def main():
    appOperador=usuario()
    return(0)

if __name__ == '__main__':
    main()
