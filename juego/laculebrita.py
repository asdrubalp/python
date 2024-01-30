import os
import time
import turtle
import random

posponer = 0.1
score = 0
hign_score = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()

#comieza la codificacion del juego
wn = turtle.Screen()
wn.title("jugo de la culebrita")
wn.bgcolor("black")
wn.setup(width=500, height=500)
wn.tracer(0)

#cabeza
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"
cabeza.color("green")

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,0)
comida.color("red")

#cuerpo
segmentos = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,200)
texto.write("Score: 0   High Score: 0", align="center", font=("Courier", 20, "normal"))

#funciones de movimiento
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def derecha():
    cabeza.direction = "right"
def izquierda():
    cabeza.direction = "left"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 10)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 10)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 10)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 10)

#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(derecha, "Right")
wn.onkeypress(izquierda, "Left")

while True:
    wn.update()
    
    
    #ventana
    if cabeza.xcor() > 230 or cabeza.xcor() < -240 or cabeza.ycor() > 230 or cabeza.ycor() < -240 :
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        
        #escorder los segmentos
        for segmento in segmentos:
            segmento.goto(1000, 1000)
            
        #borrar lista de segmento
        segmentos.clear()
        
        score = 0
        texto.clear()
        texto.write("Score: {}   High Score: {}".format(score, hign_score) , align="center", font=("Courier", 20, "normal"))
        
    if cabeza.distance(comida) < 20:
        x = random.randint(-230,230)
        y = random.randint(-230,230)
        comida.goto(x,y)
        
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.penup()
        nuevo_segmento.color("green")
        segmentos.append(nuevo_segmento)
        
        score += 10
        if score > hign_score:
            hign_score = score
        
        texto.clear()
        texto.write("Score: {}   High Score: {}".format(score, hign_score) , align="center", font=("Courier", 20, "normal"))
        
    #mover cuerpo
    totalSeg = len(segmentos)
    for i in range(totalSeg - 1, 0, -1):
        x = segmentos[i-1].xcor()
        y = segmentos[i-1].ycor()
        segmentos[i].goto(x,y)
    
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
        
    mov()
    
    #coliciones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 10:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            
            for segmento in segmentos:
                segmento.goto(1000, 1000)
            
            #borrar lista de segmento
            segmentos.clear()
            
            score = 0
            texto.clear()
            texto.write("Score: {}   High Score: {}".format(score, hign_score) , align="center", font=("Courier", 20, "normal"))
    
    time.sleep(posponer)