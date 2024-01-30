import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
print("Hola bienvenido a la calculadora para ingresar tienes que crear una cuenta")
print("¿Quieres crear una cuenta?")
print("si o no")
respuesta = input("")
if respuesta == "si":
    clear_screen()
    print("Bienvenido para crear una cuenta debes de crear un usuario y contraseña")
    usuario = input("coloca un nombre de usuario: ")
    contraseña = input("coloca una contraseña: ")
    clear_screen()
    print("felicidades has creado una cuenta")
    print("ahora para ingresar debes iniciar secion")
    print("¿Quieres iniciar secion?")
    print("si o no")
    respuesta1 = input("")
    if respuesta1 == "si":
        clear_screen()
        for i in range(2):
            print("vamos a iniciar secion coloca tu nombre de usuario y contraseña")
            user = input("Ponto tu usuario: ")
            if user == usuario: 
                for i in range(2):
                    password = input("Pon tu contraseña: ")
                    if password == contraseña:
                        clear_screen()
                        print("bienvenido a la calculadora "+usuario)
                        for i in range(1000000):
                            print("Seleccione la operacion que desea realizar")
                            print("1.Sumar"); print("2.Restar"); print("3.Multiplicar"); print("4.Dividir"); print("5.salir")
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
                            elif operacion == "multiplicar":
                                clear_screen()
                                num1 = float(input("Ingrese el primer numera de la multiplicacion: "))
                                num2 = float(input("Ingrese el segundo numera de la multiplicacion: "))
                                resultado = num1 * num2 
                                print(f"el resultado de la multiplicacion es {resultado}")
                            elif operacion == "dividir":
                                clear_screen()
                                num1 = float(input("Ingrese el primer numera de la divicion: "))
                                num2 = float(input("Ingrese el segundo numera de la divicion: "))
                                resultado = num1 / num2 
                                print(f"el resultado de la divicionn es {resultado}")
                            elif operacion == "salir":
                                clear_screen()
                                print("bye "+usuario)
                                sys.exit()
                    else:
                        print("error de contraseña")
            else:
                print("Usuario incorecto intente de nuevo")
    elif respuesta1 == "no": 
        clear_screen()
        print("bye")
        sys.exit()
elif respuesta == "no":
    clear_screen()
    print("bye")
    sys.exit()