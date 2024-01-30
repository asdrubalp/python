import sqlite3
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()

def calculadora():
    print("Seleccione la operacion que desea realizar")
    print("1.suma"); print("2.resta"); print("3.multiplicacion"); print("4.divicion"); print("5.salir")
    operacion = input("Ingrese su operacion a realizar: ")
    if operacion == "suma":
        clear_screen()
        num1 = float(input("Ingrese el primer numera de la suma: "))
        num2 = float(input("Ingrese el segundo numera de la suma: "))
        resultado = num1 + num2 
        print(f"el resultado de la suma es {resultado}")
    elif operacion == "resta":
        clear_screen()
        num1 = float(input("Ingrese el primer numera de la resta: "))
        num2 = float(input("Ingrese el segundo numera de la resta: "))
        resultado = num1 - num2 
        print(f"el resultado de la resta es {resultado}")
    elif operacion == "multiplicacion":
        clear_screen()
        num1 = float(input("Ingrese el primer numera de la multiplicacion: "))
        num2 = float(input("Ingrese el segundo numera de la multiplicacion: "))
        resultado = num1 * num2 
        print(f"el resultado de la multiplicacion es {resultado}")
    elif operacion == "divicion":
        clear_screen()
        num1 = float(input("Ingrese el primer numera de la divicion: "))
        num2 = float(input("Ingrese el segundo numera de la divicion: "))
        resultado = num1 / num2 
        print(f"el resultado de la divicionn es {resultado}")
    elif operacion == "salir":
        clear_screen()
        print("bye "+user)
        sys.exit()

def createdb():
    conexcion = sqlite3.connect('base-de-datos.db')
    conexcion.commit()
    conexcion.close()

def createtable():
    Conexcion = sqlite3.connect('base-de-datos.db')
    cursor = Conexcion.cursor()
    cursor.execute("""CREATE TABLE usuarios(nombre TEXT, contraseña INTEGER)""")
    Conexcion.commit()
    Conexcion.close()

def insertRow(nombre_del_usuario, contraseña_del_usuario):
    Conexcion = sqlite3.connect('base-de-datos.db')
    cursor = Conexcion.cursor()
    intruccion = str(f"INSERT INTO usuarios VALUES ('{nombre_del_usuario}',{contraseña_del_usuario})")
    cursor.execute(intruccion)
    Conexcion.commit()
    Conexcion.close()

if __name__ == '__main__':
    #createdb()
    #createtable()
    print("Hola bienvenido a la calculadora para ingresar tienes que tener una cuenta")
    print("¿tienes una cuenta?")
    print("si o no")
    respuesta = input("")
    if respuesta == "no":
        clear_screen()
        print("¿Quieres crear una cuenta?")
        print("si o no")
        respuesta = input("")
        if respuesta == "si":
            clear_screen()
            print("Bienvenido para crear una cuenta debes de crear un usuario y contraseña")
            for i in range(50):
                user = input("escribe el nombre de usuario ")
                def usuariodb():
                    Conexcion = sqlite3.connect('base-de-datos.db')
                    cursor = Conexcion.cursor()
                    intruccion = f"SELECT nombre FROM usuarios WHERE nombre='{user}'"
                    cursor.execute(intruccion)
                    resultado = cursor.fetchone()
                    Conexcion.commit()
                    Conexcion.close()
                    return resultado
                usuario = usuariodb()
                if (f'{user}',) == usuario:
                    print("el nombre de usuario ya existe ingrese otro ")
                else:
                    insertRow(
                        nombre_del_usuario = input("vuelva a escribe el nombre de usuario "),
                        contraseña_del_usuario = float(input("escribe una contraseña numerica "))
                    )
                    clear_screen()
                    print("felicidades has creado una cuenta")
                    print("ahora para ingresar debes iniciar secion")
                    print("¿Quieres iniciar secion?")
                    print("si o no")
                    respuesta = input("")
                    if respuesta == "si":
                        clear_screen()
                        for i in range(2):
                            print("vamos a iniciar secion coloca tu nombre de usuario y contraseña")
                            user = input("escribe tu nombre de usuario ")
                            def usuariorow():
                                Conexcion = sqlite3.connect('base-de-datos.db')
                                cursor = Conexcion.cursor()
                                intruccion = f"SELECT nombre FROM usuarios WHERE nombre='{user}'"
                                cursor.execute(intruccion)
                                resultado = cursor.fetchone()
                                Conexcion.commit()
                                Conexcion.close()
                                return resultado
                            usuario = usuariorow()
                            if (f'{user}',) == usuario:
                                for i in range(2):
                                    password = float(input("escribe tu contraseña numerica "))
                                    def contraseñarow():
                                        Conexcion = sqlite3.connect('base-de-datos.db')
                                        cursor = Conexcion.cursor()
                                        intruccion = f"SELECT * FROM usuarios WHERE contraseña={password}"
                                        cursor.execute(intruccion)
                                        resultado = cursor.fetchone()
                                        Conexcion.commit()
                                        Conexcion.close()
                                        return resultado
                                    contraseña = contraseñarow()
                                    if (f'{user}', password) == contraseña :
                                        clear_screen()
                                        print("bienvenido a la calculadora "+user)
                                        for i in range(1000000):
                                            calculadora()
                                    else:
                                        clear_screen()
                                        print("error de contraseña")
                            else:
                                clear_screen()
                                print("Usuario incorecto intente de nuevo")
                    elif respuesta == "no": 
                        clear_screen()
                        print("bye")
                        sys.exit()
        elif respuesta == "no":
            clear_screen()
            print("bye")
            sys.exit()
    elif respuesta == "si":
            clear_screen()
            print("¿desea iniciar secion?")
            print("si o no")
            respuesta = input("")
            if respuesta == "si":
                clear_screen()
                for i in range(2):
                    print("vamos a iniciar secion coloca tu nombre de usuario y contraseña")
                    user = input("escribe tu nombre de usuario ")
                    def usuariorow():
                        Conexcion = sqlite3.connect('base-de-datos.db')
                        cursor = Conexcion.cursor()
                        intruccion = f"SELECT nombre FROM usuarios WHERE nombre='{user}'"
                        cursor.execute(intruccion)
                        resultado = cursor.fetchone()
                        Conexcion.commit()
                        Conexcion.close()
                        return resultado
                    usuario = usuariorow()
                    if (f'{user}',) == usuario:
                        for i in range(2):
                            password = float(input("escribe tu contraseña numerica "))
                            def contraseñarow():
                                Conexcion = sqlite3.connect('base-de-datos.db')
                                cursor = Conexcion.cursor()
                                intruccion = f"SELECT * FROM usuarios WHERE contraseña={password}"
                                cursor.execute(intruccion)
                                resultado = cursor.fetchone()
                                Conexcion.commit()
                                Conexcion.close()
                                return resultado
                            contraseña = contraseñarow()
                            if (f'{user}', password) == contraseña:
                                clear_screen()
                                print("bienvenido a la calculadora "+user)
                                for i in range(1000000):
                                    calculadora()
                            else:
                                clear_screen()
                                print("error de contraseña")
                    else:
                        clear_screen()
                        print("Usuario incorecto intente de nuevo")
            elif respuesta == "no":
                clear_screen()
                print("bye")
                sys.exit()