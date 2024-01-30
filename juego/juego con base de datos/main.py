import sqlite3
import sys
import os
import turtle
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()

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
    createdb()
    createtable()